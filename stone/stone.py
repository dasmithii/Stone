"""Usage:
	stone read <txid> [--tor]
	stone write (--path=<> | --data=<>) [--tor]
	stone price (--path=<> | --data=<>)
	stone (-h | --help)
	stone --version

Options:
	-h, --help     Show this screen.
	--version      Show version.
	--data=<>      Specify content in string form.
	--path=<>      Specify path to content.
	--tor          Perform operation over the Tor network. [default: False]
"""
from docopt import docopt
import btc


def data(args):
	if args['--data'] is not None:
		return args['--data']
	with open(args['--path']) as f:
		return f.read()


def main():
	args = docopt(__doc__, version='Yamba 0.0.1')

	if args['price']:
		amount = btc.price_without_fee(data(args))
		output = '{:5.7f} - (w/o transaction fees)'.format(amount)
		print(output)
	elif args['read']:
		print(btc.read(args['<txid>'], args['--tor']))
	elif args['write']:
		print(btc.publish(data(args), args['--tor']))
	else:
		print(__doc__)

if __name__ == '__main__':
	main()