import unittest
from autocomplete import *
import random, string
from random import randint


class TestAutocomplete(unittest.TestCase):
	#Tests for autocomplete.py

		def test_no_word_added(self):
			root = Trie()
			self.assertEqual(root.find_top_k(5, 'ke'), [])

		def test_only_one_word_added(self):
			root = Trie()
			root.insert('statistics', 10)
			self.assertEqual(root.find_top_k(1, 'k'), [])
			self.assertEqual(root.find_top_k(1, 's'), [(10, 'statistics')])
			self.assertEqual(root.find_top_k(5, 's'), [(10, 'statistics')])

		def test_insert_same_words(self):
			root = Trie()
			root.insert('kevin', 15)
			root.insert('kevin', 30)
			root.insert('kechup', 18)
			self.assertEqual(root.find_top_k(1, 'k'), [(30, 'kevin')])
			self.assertEqual(root.find_top_k(3, 'k'), [(30, 'kevin'), (18, 'kechup')])

		def test_word_breeds_another(self):
			root = Trie()
			root.insert('kev', 10)
			root.insert('kevin', 15)
			root.insert('kevinrocks', 20)
			self.assertEqual(root.find_top_k(3, 'ke'), [(20, 'kevinrocks'), (15, 'kevin'), (10, 'kev')])

		def test_function_contains(self):
			root = Trie()
			root.insert('stat', 50)
			root.insert('john', 20)
			root.insert('kevin', 35)
			self.assertTrue(root.contains('stat'))
			self.assertFalse(root.contains('ted'))

		def test_case_insensitive(self):
			root = Trie()
			root.insert('Kevin', 20)
			root.insert('kebab', 30)
			self.assertEqual(root.find_top_k(1, 'Ke'), [(30, 'kebab')])

		#Insert randomized test by inserting randomly assigned 100 dictionary values

		def test_random_word_inserted(self):
			root = Trie()
			list_words = []

			for i in range(0, 100):

				random_word = ''.join(random.choice(string.lowercase) for i in range(0, randint(1, 15)))
				random_weight = randint(0, 1000000)	
				root.insert(random_word, random_weight)
				list_words.append((random_weight, random_word))
			
			# Sort the list by using traditional function, and get first five items
			sorted_list = sorted(list_words, key=lambda x: (-x[0]))[0:5]
			self.assertEqual(root.find_top_k(5, ''), sorted_list)



if __name__ == '__main__':
    unittest.main()

