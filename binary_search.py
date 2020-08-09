import random
from time import time, time_ns
import unittest
import matplotlib.pyplot as plt
import pandas as pd
import more_itertools as mit
import numpy as np

# Binary Search Algorithm

def binary_search(data, value):
    l= 0
    r= len(data)-1

    while(l <= r):
        
        mid = (l+r) // 2
        
        if(data[mid] == value):
            return mid
        
        elif value > data[mid]:
            l = mid+1
            
        elif value < data[mid]:
            r = mid-1
            
    return -1

# Unit Testing Implementation
class TestSearch(unittest.TestCase):
    
    def test_search(self):
        data = [2,3,4,5,6,7,8,12]
        self.assertEqual(binary_search(data,5),3)
        
    def test_searchChar(self):
        data = ['a','b','x','z']
        self.assertEqual(binary_search(data, 'x'),2)

if __name__ == "__main__":
    unittest.main()


# Binary Search Implementation
    
input_size = []

execution_time_best = []
execution_time_worst = []

size = 10000
MIN = 10000
MAX = 10000000

while size <= 1000000:  
    input_size.append(size)   
    
    # create a sample of sorted data  
    data = random.sample(range(MIN, MAX),size)
    data.sort()
    
    # for best case 
    start_time = time()
    index_best = binary_search(data, data[size//2])
    end_time = time()
    elapsed_time_best = (end_time - start_time)
    
    execution_time_best.append(elapsed_time_best)
    
    # for worst case
    start_time = time_ns()
    index_worst = binary_search(data, -1) 
    end_time = time_ns()
    elapsed_time_worst = (end_time - start_time) 
    
    execution_time_worst.append(elapsed_time_worst)
    
    size = size + 10000  # step-size is 10,000    

# Results
input_df = pd.DataFrame(input_size, columns = ['input-size'])
best_case_df = pd.DataFrame(execution_time_best, columns = ['best-case'])
worst_case_df = pd.DataFrame(execution_time_worst, columns = ['worst-case'])

result = pd.concat([input_df, best_case_df, worst_case_df], axis=1)
print(result)


# Plotting the input-size VS execution-time (for best-case)
fig3, ax3 = plt.subplots()
ax3.plot(input_size, execution_time_worst, color='red', marker = "o", ls="")
ax3.autoscale(enable=True, axis="y", tight=False)
plt.title('Input-size VS execution-time for Best case of linear search')
plt.xlabel('Input Size')
plt.ylabel('Execution Time')
plt.plot(input_size, execution_time_best, c = 'green')
plt.show()


# Plotting the input-size VS execution-time (for worst-case)
fig3, ax3 = plt.subplots()
ax3.plot(input_size, execution_time_worst, color='red', marker = "o", ls="")
ax3.autoscale(enable=True, axis="y", tight=False)
plt.title('Input-size VS execution-time for Worst case of linear search')
plt.xlabel('Input Size')
plt.ylabel('Execution Time')
plt.show()

    
    
    