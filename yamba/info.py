import tor

def query(call):
	"""Query blockchain.info"""
	return tor.query('http://blockchain.info/q/' + call)


def block_count():
	return int(query('getblockcount'))

