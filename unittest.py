

import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(findInterval(1.8, [2.0, 5.0, 8.0, 10]), -1)
    def test2(self):
        self.assertEqual(findInterval(5, [2, 3.0, 6.5, 8]), 1)
    def test3(self):
        self.assertEqual(findInterval(10, [1,3,3,5]), 3)
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Test('test1')) 
    suite.addTest(Test('test2'))
    suite.addTest(Test('test3'))
    unittest.TextTestRunner().run(suite)




