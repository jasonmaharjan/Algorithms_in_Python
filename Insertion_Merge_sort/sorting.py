def insertionSort(data):
   n = len(data)
   for j in range(1, n):
      key = data[j]

      # insert data[j] into the sorted sequence
      i = j-1
      while i >= 0 and data[i] > key:
         data[i+1] = data[i]
         i -= 1

      data[i+1] = key
   