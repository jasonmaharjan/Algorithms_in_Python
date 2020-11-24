import unittest
from knapsack import bruteforce, frac_greedy, dynamic

class Knapsack(unittest.TestCase):

   def test_bruteforce(self):
      p = [5, 6, 7, 2]
      w = [4, 2, 3, 1]  
      m = 8

      input = bruteforce(p,w,m)
      output = ['0111', 15]
      self.assertListEqual(input, output)

   def test_frac_bruteforce(self):
      p = [110, 120, 2]
      w = [6, 7, 3]  
      m = 10

      input = bruteforce(p,w,m)
      output = [178, ['1', '34.29%'. '0']]
      self.assertListEqual(input, output)
   
   def test_greedy(self):
      p = [5, 6, 7, 2]
      w = [4, 2, 3, 1]  
      m = 8

      input = frac_greedy(p,w,m)
      output = [[0.5, 1, 1, 1], 17.5]
      self.assertListEqual(input, output)

   def test_dynamic(self):
      p = [21, 16, 27, 12]
      w = [4, 10, 13, 7]  
      m = 20

      input = dynamic(p,w,m)
      output = 48
      self.assertEqual(input, output)


if __name__ == '__main__':
   unittest.main()
   
