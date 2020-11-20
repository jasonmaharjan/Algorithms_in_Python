import unittest
from sorting import insertionSort
from sorting import mergeSort

class SortingTestCase(unittest.TestCase):

   def test_insertion_sort(self):
      input = [10, 2, 13, 8, 16, 14]
      output = [2, 8, 10, 13, 14, 16]

      #insertionSort(input)
      mergeSort(input, 0, 5)
      self.assertListEqual(input,output)

if __name__ == '__main__':
   unittest.main()
   
