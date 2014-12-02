import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "stone",
    version = "0.0.1",
    author = "Adam Smith",
    author_email = "dsmith2@wpi.edu",
    description = ("anonymous publishing via Tor onto the Blockchain"),
    license = "WTFPL",
    keywords = ['Tor', 'Bitcoin', 'BTC', 'anonymous', 'publishing', 'write'],
    packages=['stone'],
    long_description=read('README'),
    entry_points = {
        'console_scripts': ['stone=stone.main:main']
    }
)