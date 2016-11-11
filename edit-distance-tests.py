#!/usr/bin/env python

import unittest
from edit_distance import *

#Tests for edit_distance.py

class TestEditDistance(unittest.TestCase):	
	#Tests whether same word edit returns 0
	def test_same_word(self):
		self.assertEqual(edit_distance('kevin', 'kevin'), 0)
		self.assertEqual(edit_distance('john', 'john'), 0)

	#Tests substitution
	def test_substitution(self):
		self.assertEqual(edit_distance('back', 'jack'), 1)
		self.assertEqual(edit_distance('kite', 'kate'), 1)

	#Tests insertion/deletion
	def test_edit_insertion(self):
		self.assertEqual(edit_distance('pace', 'space'), 1)
		self.assertEqual(edit_distance('son', 'sloan'), 2)
		self.assertEqual(edit_distance('kin', 'kevin'), 2)

	#Tests case-insensitivity
	def test_edit_case_insensitive(self):
		self.assertEqual(edit_distance('kitten', 'Knitting'),3)
		self.assertEqual(edit_distance('blaCk', 'Black'), 0)

	#Tests selected word
	def test_selected_words(self):
		test_cases = zip(['islander','mart','kitten','intention'], 
			             ['slander', 'karma','sitting','execution'],
			             [1,3,3,5])
		for i in range(len(test_cases)):
			self.assertEqual(edit_distance(test_cases[i][0], test_cases[i][1]), test_cases[i][2])

if __name__ == '__main__':
    unittest.main()