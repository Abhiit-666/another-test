import unittest
import add

class TestCalc(unittest.TestCase):
	def test_add(self):
		result=add.add(10,5)
		self.assertEqual(result,5)

if __name__ =='__main__':
	unittest.main()
