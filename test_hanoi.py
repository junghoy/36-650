import unittest
from hanoi import *



class TestAutocomplete(unittest.TestCase):
	#Tests for hanoi.py

		#Tests the base case
		def test_base_case(self):

			self.assertEqual(hanoi(1, 'L', 'M', 'N', movefn, list()), [(1, 'L', 'N')])

		#Tests whether the first move is valid
		def test_first_move(self):

			hanoi_4 = hanoi(4, 'L', 'M', 'N', movefn, list())
			start = hanoi_4[0][1]
			moved_to = hanoi_4[0][2]
			self.assertEqual(start, 'L')
			self.assertTrue(moved_to in ['M', 'N'])
		
			hanoi_5 = hanoi(5, 'L', 'M', 'N', movefn, list())
			start = hanoi_5[0][1]
			moved_to = hanoi_5[0][2]
			self.assertEqual(start, 'L')
			self.assertTrue(moved_to in ['M', 'N'])

		#Tests whether the last move is valid
		def test_last_move(self):

			hanoi_4 = hanoi(4, 'L', 'M', 'N', movefn, list())
			start = hanoi_4[len(hanoi_4)-1][1]
			moved_to = hanoi_4[len(hanoi_4)-1][2]
			self.assertTrue(start in ['L', 'M'])
			self.assertEqual(moved_to, 'N')

			hanoi_5 = hanoi(5, 'L', 'M', 'N', movefn, list())
			start = hanoi_5[len(hanoi_5)-1][1]
			moved_to = hanoi_5[len(hanoi_5)-1][2]
			self.assertTrue(start in ['L', 'M'])
			self.assertEqual(moved_to, 'N')

		#Tests whether the number of moves is correct
		#Our algorithm tells us that the number of moves should be 2^n-1
		def test_number_moves(self):

			for i in range(1, 10):

				self.assertEqual(len(hanoi(i, 'L', 'M', 'N', movefn, list())), 2**i-1)
				


if __name__ == '__main__':
    unittest.main()

		