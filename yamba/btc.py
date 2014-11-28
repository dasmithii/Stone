import protocol
import bitcoin.rpc
import subprocess


def publish(data):
	"""Encode data via protocol.py and attempt to publish it to
	the main blockchain within one transaction of many outputs.

	This is a hacky approach, using a subprocess shell call in
	place of the bitcoin library - because the bitcoin library
	doesn't currently provide a sendmany interface. Hopefully
	this will change soon.
	"""
	addresses = protocol.encode(data)
	proxy = bitcoin.rpc.Proxy()
	def prepare(x):
		return '"' + x + '"' + ':' + '0.00005430'
	amounts = '{' + ','.join(map(prepare, addresses)) + '}'
	process = subprocess.Popen(['bitcoin-cli', 'sendmany', '', amounts] , stdout=subprocess.PIPE,
		                                                                  stderr=subprocess.PIPE)
	o, e = process.communicate()
	return {
		'output': o,
		'error': e
	}
