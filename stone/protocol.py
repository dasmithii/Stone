import zlib
import hashlib
import binascii
from bitcoin import base58
import bitcoin.core


VERSION = '1'


CHARACTERS_IN_ADDRESS = 34
BYTES_IN_PAYLOAD = 20

def squeeze(data):
	"""Forms a valid bitcoin address around the given data bytes by
	postfixing them after the version byte, hashing this combination, 
	postfixing that hash, and base58 encoding the resulting string.
	"""
	if len(data) != BYTES_IN_PAYLOAD:
		raise BaseException('invalid payload length: %d - should be %d' % (len(data), BYTES_IN_PAYLOAD))
	if bitcoin.core.coreparams.NAME == 'mainnet':
		data = chr(0) + data
	elif bitcoin.core.coreparams.NAME == 'testnet':
		data = chr(111) + data 
	else:
		raise 'invalid network mode'
	data += bitcoin.core.Hash(data)[0:4]
	return base58.encode(data)

def extract(address):
	"""Returns original form of bitcoin address payload."""
	return base58.decode(address)[1:-4]



MARKED_REGULAR = '0'
MARKED_COMPRESSED = '1'

def mark_compressed(data):
	return MARKED_COMPRESSED + data

def mark_regular(data):
	return MARKED_REGULAR + data

def is_compressed(data):
	return data[0] == MARKED_COMPRESSED

def is_regular(data):
	return data[0] == MARKED_REGULAR

def compress(data):
	z = zlib.compress(data)
	if len(z) < len(data):
		return mark_compressed(z)
	return mark_regular(data)

def decompress(data):
	if is_compressed(data):
		return zlib.decompress(data[1:])
	return data[1:]


def pad(data):
	"""Lengthens the given string to the next multiple of
	BYTES_IN_PAYLOAD. This is done by appending zeros and prepending
	a single byte to indicate the number of zeros appended.
	"""
	offset = BYTES_IN_PAYLOAD - ((len(data) + 1) % BYTES_IN_PAYLOAD)
	target = len(data) + offset
	data = data.ljust(target, '0')
	data = chr(offset) + data
	return data

def unpad(data):
	"""Reverses pad()."""
	padding = ord(data[0])
	return data[1:-padding]

def encode(data):
	"""Compresses and pads data before distributing it accross
	a series of valid bitcoin addresses.
	"""
	data = VERSION + data
	compressed = compress(data)
	padded = pad(compressed)
	parts = [padded[i:i+BYTES_IN_PAYLOAD] for i in range(0, len(padded), BYTES_IN_PAYLOAD)]
	return map(squeeze, parts)

def decode(addresses):
	"""Reverses the encoding process, rejoining, unpadding, and
	decompressing data.
	"""
	parts = map(extract, addresses)
	padded = ''.join(parts)
	compressed = unpad(padded)
	decompressed = decompress(compressed)
	version, data = decompressed[0], decompressed[1:]
	if version != VERSION:
		raise BaseException("versions don't match")
	return decompress(compressed)[1:]
