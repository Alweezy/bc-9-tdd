import unittest
from my_sum import my_sum

class MySumTests(unittest.TestCase):

	def setUp(self):
	 	#setting up
		self.numbers = [10,5,7,8,90,60]
	def test_sum_of_numbers(self):

		'''
		Test sum of digits or numbers
		'''
	 
		self.assertEqual(my_sum(5,10), 15, msg='should return 25')

		self.assertEqual(my_sum(15,10), 25, msg='should return 25')

		self.assertEqual(my_sum(25,10), 35, msg='should return 25')

		self.assertEqual(my_sum(35,10), 45, msg='should return 25')

		self.assertEqual(my_sum(45,10), 55, msg='should return 25')

		self.assertEqual(my_sum(55,10), 65, msg='should return 25')


	def test_non_numbers(self):
		"""
		Asset throwing exceptions when it is a test_non_numbers
		"""
		with self.assertRaises(TypeError):
			my_sum('10',15)
			my_sum(10,'15')
			my_sum('10','15')

if __name__ == '__main__':
	unittest.main()
#this if_main function,it automates the test.
