import random
from time import time
import unittest
import matplotlib.pyplot as plt
import pandas as pd

# Linear Search Algorithm
def linear_search(data, value):
    for i in range(len(data)):
        if data[i] == value:
            return i
    return -1  
  
      
# Unit Testing Implementation
class TestSearch(unittest.TestCase):
    
    def test_search(self):
        data = [2,3,4,5,6,7,8,12]
        self.assertEqual(linear_search(data,3),1)
        
    
    def test_searchChar(self):
        data = ['a','b','x','z']
        self.assertEqual(linear_search(data, 'x'),2)

if __name__ == "__main__":
    unittest.main()


# Linear Search Implementation
input_size = []

execution_time_best = []
execution_time_worst = []

size = 10000
MIN = 10000
MAX = 10000000

while size <= 1000000:
    input_size.append(size)   
    data = random.sample(range(MIN, MAX),size)
    
    # for best case
    start_time = time()
    index_best = linear_search(data, data[0])
    end_time = time()
    elapsed_time_best = end_time - start_time
    
    execution_time_best.append(elapsed_time_best)
    
    # for worst case
    start_time = time()
    index_worst = linear_search(data, data[size-1])
    end_time = time()
    elapsed_time_worst = end_time - start_time    
    
    execution_time_worst.append(elapsed_time_worst)
    print(elapsed_time_worst)
    
    size = size + 10000    # Step size is 10,000

# Results
input_df = pd.DataFrame(input_size, columns = ['input-size'])
best_case_df = pd.DataFrame(execution_time_best, columns = ['best-case'])
worst_case_df = pd.DataFrame(execution_time_worst, columns = ['worst-case'])

result = pd.concat([input_df, best_case_df, worst_case_df], axis=1)
print(result)

# Plotting the input-size VS execution-time (for best-case)
plt.figure(figsize=(12,8))
plt.title('Input-size VS execution-time for Best case of linear search')
#plt.scatter(input_size, execution_time_best, c = 'green')
plt.xlabel('Input Size')
plt.ylabel('Execution Time')
plt.plot(input_size, execution_time_best, c = 'green')
plt.show()

# Plotting the input-size VS execution-time (for worst-case)
plt.figure(figsize=(12,8))
plt.title('Input-size VS execution-time for Worst case of linear search')
#plt.scatter(input_size, execution_time_worst, c = 'red')
plt.xlabel('Input Size')
plt.ylabel('Execution Time')
plt.plot(input_size, execution_time_worst, c = 'red')
plt.show()