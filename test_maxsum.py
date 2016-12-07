#!/usr/bin/env python

import unittest
from maxsum import maxSubSum

#Tests for maxsum.py

class TestAutocomplete(unittest.TestCase):
	
	#Tests the base case
	def test_base_case(self):
		self.assertEqual(maxSubSum([]), 0)

	#Tests increasing sequence
	def test_increasing_subsequence(self):
		self.assertEqual(maxSubSum([1,2,3,4]), 10)
		self.assertEqual(maxSubSum([3,5,7,9]), 24)

	#Tests whether list of all negative numbers return 0
	def test_all_negative(self):
		self.assertEqual(maxSubSum([-1,-2,-3]), 0)
		
	#Tests alternating positive / negative sequence
	def test_alternating(self):
		self.assertEqual(maxSubSum([-1,1,-1,1,-1,1,-1]), 1)

	def test_decimal(self):
		self.assertEqual(maxSubSum([1.2,2.4,-3.6,4.8,6.0,-2.0,7.2,-9.6]), 16.0)

	def test_complex(self):
		self.assertEqual(maxSubSum([31,-41,59,26,-53,58,97,-93,-23,84]), 187)

if __name__ == '__main__':
    unittest.main()

		