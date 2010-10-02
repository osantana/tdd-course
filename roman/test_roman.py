import unittest

from roman import to_roman

class TestRoman(unittest.TestCase):
    def test_zero(self):
        self.assertEquals("", to_roman(0))

    def test_one(self):
        self.assertEquals("I", to_roman(1))

    def test_two(self):
        self.assertEquals("II", to_roman(2))

    def test_three(self):
        self.assertEquals("III", to_roman(3))