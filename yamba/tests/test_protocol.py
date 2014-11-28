import unittest
from .. import protocol as p
import os
import random


def random_bytes(n):
  return os.urandom(n)

def random_data(min=1, max=1000):
  n = random.randint(min, max)
  return random_bytes(n)


def form_inverse(f1, f2):

  class i(unittest.TestCase):

    def on(self, data):
      return f1(data)

    def off(self, data):
      return f2(data)

    def test(self):
      def test_with(data):
        w1 = self.on(data)
        w2 = self.off(w1)
        self.assertEqual(data, w2)

      for i in range(25):
        test_with(random_data())

  return i

Test_compression = form_inverse(p.compress, p.decompress)
Test_padding = form_inverse(p.pad, p.unpad)
Test_protocol = form_inverse(p.encode, p.decode)
