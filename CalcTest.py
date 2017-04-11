import unittest
from calculator import Calculator

def setUpModule():
  print('set up module')

def tearDownModule():
  print('tear down module')

class TestCalculator(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    print('Set up class')
    # Create an instance of the calculator that can be used in all tests

  @classmethod
  def tearDownClass(self):
    print('Tear down class')

  def test_add(self):
    calc=Calculator()
    self.assertEqual(calc.add(2, 7), 9)

  # Write test methods for subtract, multiply, and divide
  def test_subtract(self):
    calc=Calculator()
    self.assertEqual(calc.subtract(7,2), 5)

  def test_multiply(self):
    calc=Calculator()
    self.assertEqual(calc.multiply(2,7), 14)

  def test_divide(self):
    calc=Calculator()
    self.assertEqual(calc.divide(10,5), 2)
    

if __name__ == '__main__':
    unittest.main()