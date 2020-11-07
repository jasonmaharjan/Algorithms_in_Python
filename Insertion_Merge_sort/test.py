import unittest
from sorting import insertionSort

class SortingTestCase(unittest.TestCase):

   def test_insertion_sort(self):
      input = [3, 2, 1, 5, 4]
      output = [1, 2, 3, 4, 5]

      insertionSort(input)

      self.assertListEqual(input,output)

if __name__ == '__main__':
   unittest.main()