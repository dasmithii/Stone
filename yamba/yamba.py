"""Yamba

Usage:
	yamba price (--path=<> | --data=<>)
	yamba --wallet=<> (--path=<> | --data=<>)
	yamba feed [--from=<>]
	yamba cat <document>

Options:
	-h --help       Show this screen.
	-v --version    Show version.
	--data=<>    Specify content in string form.
	--path=<>       Specify path to content.
	--wallet=<>     Specify BTC wallet to pay with.
	--from=<>       Specify begin date and time.      [default: now]
	--document=<>   Look up by sender address.
"""
from docopt import docopt
import tor

def main():
	args = docopt(__doc__, version='Yamba 0.0.1')
	print tor.query("http://dasmithii.github.io/journal/writings/Disclaimer.txt")

if __name__ == '__main__':
	main()