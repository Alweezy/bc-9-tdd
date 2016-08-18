import unittest
from super_sum import super_sum

class SuperSum(unittest.TestCase):
	
	def setUp(self):
	 	#setting up
		self.numbers = [10,5,7,8,90,60]
	def test_check_error(self):
		self.assertEqual(super_sum([6,'Beta']), "Invalid type" )
	def test_sum_of_integers(self):
		self.assertEqual(super_sum(10, 5, 6, 9), 30)
		self.assertEqual(super_sum([5, 6], [4, 5], 10), 30)
		self.assertEqual(super_sum([10, 5], 5), 20)
	def test_empty(self):
		self.assertEqual(super_sum() ,"You must pass an argument")
	
if __name__ == '__main__':
	unittest.main()
#this if_main function,it automates the test.
