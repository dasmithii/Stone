import info
import protocol
import bitcoin.rpc
import subprocess


def price_without_fee(data):
	addresses = protocol.encode(data)
	return 0.00005430 * len(addresses)


def write(data, tor=False):
	"""Encode data via protocol.py and attempt to publish it on
	the blockchain within one transaction of many outputs.
	"""
	if tor:
		raise NotImplementedError('Tor for writing')

	proxy = bitcoin.rpc.Proxy()
	addresses = protocol.encode(data)
	mapping = {}
	for address in addresses:
		mapping[address] = 0.00005430
	return proxy.sendmany('', mapping)


def trusted_read(txid, go_anon=False):
	"""Reads transaction via blockchain.info API. 

	This is nice because it doesn't require that callers have run
	Bitcoin nodes on their machines. But it is dangerous, too, as
	it relies on a centralized server. Use wallet_read() or 
	local_read() whenever possible.
	"""
	info.using_tor = go_anon
	transaction = info.transaction(txid)
	addresses = []
	for o in transaction['out']:
		if o['value'] == 5430:
			addresses.append(o['addr'])
	return protocol.decode(addresses)


def read(txid, tor=False):
	"""Decode data from transaction.

	Depending on the configuration of bitcoind, non-wallet 
	transactions may or may not be visible. If they aren't
	query blockchain.info instead.

	TODO: FINISH IMPLEMENTING
	"""
	return trusted_read(txid, tor)