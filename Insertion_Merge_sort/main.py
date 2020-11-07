from random import sample
from sorting import insertionSort
from time import time_ns
import matplotlib.pyplot as plt
import pandas as pd

# Execution Time Calculation
def run(n):
   data = sample(range(n+1), n)
   start_time = time_ns()
   insertionSort(data)
   end_time = time_ns()

   time_taken = end_time - start_time
   print(time_taken)
   execution_time.append(time_taken)


if __name__ == '__main__':
   A = 1000
   B = 20001
   step = 1000
   input_size = []
   execution_time = []
   
   for i in range(A, B, step):
       input_size.append(A)
       run(A)
       A += step

# Convert results into dataframes
input_df = pd.DataFrame(input_size, columns = ['input-size'])
time_df = pd.DataFrame(execution_time, columns = ['execution-time'])
result = pd.concat([input_df, time_df], axis=1)

# Plotting the input-size VS execution-time 
plt.figure(figsize=(12,8))
plt.title('Input-size VS execution-time for Insertion Sort')
#plt.scatter(input_size, execution_time_best, c = 'green')
plt.xlabel('Input Size')
plt.ylabel('Execution Time')
plt.plot(input_size, execution_time, c = 'green')
plt.show()
    
    