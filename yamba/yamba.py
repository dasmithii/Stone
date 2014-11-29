"""Yamba

Usage:
	yamba cost (--path=<> | --data=<>)
	yamba --wallet=<> (--path=<> | --data=<>) [--tor]
	yamba cat <txid> [--tor]

Options:
	-h --help           Show this screen.
	-v --version        Show version.
	--data=<>           Specify content in string form.
	--path=<>           Specify path to content.
	--wallet=<>         Specify BTC wallet to pay with.
	--tor               Perform operation over the Tor network. [default: False]
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

	if args['cost']:
		amount = btc.price_without_fee(data(args))
		output = '{:5.7f} - (w/o transaction fees)'.format(amount)
		print(output)
	elif args['cat']:
		print btc.read(args['<txid>'], args['--tor'])
	else:
		print btc.publish(data(args), args['--tor'])

if __name__ == '__main__':
	main()