import json
import urllib

BASE_URL = 'https://blockchain.info/'

def query(call):
	return urllib.urlopen(BASE_URL + call).read()

def block_count():
	"""Return blockchain.info's most recent block count. This is 
	useful in comparison with the local blockcount, which may be
	lagging behind."""
	return int(query('q/getblockcount'))

def transaction(txid):
	s = query('tx-index/' + txid + '?format=json')
	return json.loads(s)