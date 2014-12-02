"""Usage:
	stone [--testnet] read <txid> [--testnet] [--tor]
	stone [--testnet] write (--path=<> | --data=<>) [--testnet] [--tor]
	stone price (--path=<> | --data=<>)
	stone (-h | --help)
	stone --version

Options:
	-h, --help     Display this message.
	--version      Display version.
	--data=<>      Specify content in string form.
	--path=<>      Specify path to content.
	--tor          Perform operation over the Tor network. [default: False]
	--testnet      Run command on test network.            [default: False]
"""
from docopt import docopt
import stone
import protocol
import bitcoin



def main():
	args = docopt(__doc__, version='Yamba 0.0.1')
	if args['--testnet']:
		bitcoin.SelectParams('testnet')

	def data():
		if args['--data'] is not None:
			return args['--data']
		with open(args['--path']) as f:
			return f.read()

	if args['price']:
		amount = stone.price_without_fee(data())
		output = '{:5.7f} - (w/o transaction fees)'.format(amount)
		print(output)
	elif args['read']:
		print(stone.read(args['<txid>'], args['--tor']))
	elif args['write']:
		print(stone.write(data(), args['--tor']))
	else:
		print(__doc__)

if __name__ == '__main__':
	main()