import info
import protocol
import bitcoin.rpc
import subprocess


def price_without_fee(data):
	addresses = protocol.encode(data)
	return 0.00005430 * len(addresses)


def publish(data):
	"""Encode data via protocol.py and attempt to publish it to
	the main blockchain within one transaction of many outputs.

	This is a hacky approach, using a subprocess shell call in
	place of the bitcoin library - because the bitcoin library
	doesn't currently provide a sendmany interface. Hopefully
	this will change soon.
	"""
	addresses = protocol.encode(data)
	def prepare(x):
		return '"' + x + '"' + ':' + '0.00005430'
	amounts = '{' + ','.join(map(prepare, addresses)) + '}'
	process = subprocess.Popen(['bitcoin-cli', 'sendmany', '', amounts] , stdout=subprocess.PIPE,
		                                                                  stderr=subprocess.PIPE)
	o, e = process.communicate()
	return {
		'output': o[0:-1],
		'error': e
	}


def trusted_read(txid):
	"""Reads transaction via blockchain.info API. 

	This is nice because it doesn't require that callers have run
	Bitcoin nodes on their machines. But it is dangerous, too, as
	it relies on a centralized server. Use wallet_read() or 
	local_read() whenever possible.
	"""
	transaction = info.transaction(txid)
	addresses = []
	for o in transaction['out']:
		if o['value'] == 5430:
			addresses.append(o['addr'])
	return protocol.decode(addresses)


def read(txid):
	"""Decode data from transaction.

	Depending on the configuration of bitcoind, non-wallet 
	transactions may or may not be visible. If they aren't
	query blockchain.info instead.

	TODO: FINISH IMPLEMENTING
	"""
	return trusted_read(txid)