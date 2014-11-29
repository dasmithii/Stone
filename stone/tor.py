import atexit
import StringIO
import socket
import urllib
import socks
import ipgetter
import stem.process
from stem.util import term


#
tor_process = None


# 
def cleanup():
	if tor_process is not None:
		tor_process.kill()


# Uses urllib to fetch a site using SocksiPy for Tor over
# the SOCKS_PORT.
def query(url):
	if tor_process is None:
		prepare()
	try:
		return urllib.urlopen(url).read()
	except:
		return "Unable to reach %s" % url


# Connects to the Tor network.
def prepare():
	# Set socks proxy and wrap the urllib module
	SOCKS_PORT = 7000
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', SOCKS_PORT)
	socket.socket = socks.socksocket

	# Perform DNS resolution through the socket
	def getaddrinfo(*args):
	  return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]
	socket.getaddrinfo = getaddrinfo

	# Nicely formats Tor output.
	def print_bootstrap_lines(line):
	  if "Bootstrapped " in line:
	    print term.format(line, term.Color.BLUE)

	print term.format("Starting Tor:\n", term.Attr.BOLD)

	global tor_process
	tor_process = stem.process.launch_tor_with_config(
	  config = {'SocksPort': str(SOCKS_PORT)},
	  init_msg_handler = print_bootstrap_lines,
	)

	print term.format("\nChecking our endpoint:\n", term.Attr.BOLD)
	print term.format(query("https://www.atagar.com/echo.php"), term.Color.BLUE)


# Kill the Tor process before exiting.
atexit.register(cleanup)