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

import math
   
def mergeSort(data, p, r):
    if p < r:
        q = math.floor((p + r)/2) 
        mergeSort(data, p, q)
        mergeSort(data, q + 1, r)
        merge(data, p, q, r)
        
def merge(data, p, q, r):
    L = data[p : q + 1]
    R = data[q + 1 : r + 1]
    i = 0
    j = 0
    
    for k in range(p, r + 1):
        if i < len(L) and j < len(R):
            if L[i] <= R[j]:
                data[k] = L[i]
                i += 1
            else:
                data[k] = R[j]
                j += 1
        else:
            break
        
    if i < len(L):
        data[k : r+1] = L[i:]
        
    if j < len(R):
        data[k : r+1] = R[j:]

                
                
                
                
                
        