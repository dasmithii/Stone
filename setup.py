# # !/usr/bin/env python
# import os
# import setuptools
# from distutils.core import setup

# setup(
#     name='Yamba',
#     description='anonymous publishing',
#     author='Adam Smith',
#     author_email='dsmith2@wpi.edu',
#     version='0.0.1',
#     packages=['Yamba',],
#     license='WTFPL',
#     long_description=open('README').read(),
#     entry_points = {
#         'console_scripts': [
#             'Yamba = Yamba.Yamba:cli']
#     }
# )


import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "Yamba",
    version = "0.0.1",
    author = "Adam Smith",
    author_email = "dsmith2@wpi.edu",
    description = ("anonymous publishing via Tor onto the Blockchain"),
    license = "WTFPL",
    keywords = "Tor Bitcoin BTC anonymous publishing",
    packages=['yamba'],
    long_description=read('README'),
    entry_points = {
        'console_scripts': ['yamba=yamba.yamba:main']
    }
)