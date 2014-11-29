import tor
import json

def query(call, anon=False):
	"""Query blockchain.info"""
	return tor.query('http://blockchain.info/q/' + call)



def block_count():
	"""Return blockchain.info's most recent block count. This is 
	useful in comparison with the local blockcount, which may be
	lagging behind."""
	return int(tor.query('getblockcount'))


def transaction(txid):
	return json.loads(tor.query('http://blockchain.info/tx-index/' + txid + '?format=json'))
