import tor
import json
import urllib

BASE_URL = 'https://blockchain.info/'
using_tor = False

def tor_query(call):
	"""Query blockchain.info"""
	return tor.query(BASE_URL + call)

def regular_query(call):
	return urllib.urlopen(BASE_URL + call).read()

def query(call):
	if using_tor:
		return tor_query(call)
	return regular_query(call)

def block_count():
	"""Return blockchain.info's most recent block count. This is 
	useful in comparison with the local blockcount, which may be
	lagging behind."""
	return int(query('q/getblockcount'))


def transaction(txid):
	s = query('tx-index/' + txid + '?format=json')
	return json.loads(s)