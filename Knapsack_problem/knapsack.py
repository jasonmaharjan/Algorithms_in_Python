# Solve 0/1 Knapsack problem with Brute force 
def getStrings(n):
   return [bin(x)[2:].rjust(n, '0') for x in range(2**n)]

def bruteforce(p, w, m):
   assert len(p) == len(w), "Profit and weight do not have the same number of elements!"

   n = len(p)
   bit_strings = getStrings(n)

   max_profit = 0
   solution = ''

   result = []

   for s in bit_strings:
      profit = sum([int(s[i]) * p[i] for i in range(n)])
      weight = sum([int(s[i]) * w[i] for i in range(n)])

      if weight <= m and profit > max_profit:
         max_profit = profit
         solution = s
         
   result.append(solution)
   result.append(max_profit)

   return result

def frac_bruteforce(p,w,m):
   # For all weights, calculate the profit
   assert len(p) == len(w), "W and p not equal length"
   maxProfit = 0
   n = len(w)
   maxSeletion = ['0'] *n 
    
   solutions = getStrings(n)
    
   for s in solutions:
        
      item_rem = [i for i, x in enumerate(s) if x == '0']
        
      non_frac_profit=sum([int(s[i]) * p[i] for i in range(n)])
      weight = sum([int(s[i]) * w[i] for i in range(n)])
        
      fract_profit = 0
      temp_solution = s

      if weight<m:
         maxIndex = 0
         for i in item_rem:
            rem = m-weight if(m-weight < w[i]) else w[i]
            frac = (p[i]/w[i])*(rem)
            if frac > fract_profit:
               fract_profit = frac
               maxIndex = i
         temp_solution[maxIndex] = str(round(fract_profit/p[i],2)*100)+'%'
                
      totalProfit = fract_profit + non_frac_profit

      if weight<= m and totalProfit >= maxProfit:
         maxProfit = totalProfit
         maxSeletion = temp_solution

   return (int(maxProfit),('|'.join(maxSeletion)).split('|'))

# Solve fractional knapsack using Greedy Algorithm
class ItemValue:

   def __init__(self, p, w, index):
      self.p = p
      self.w = w
      self.index = index
      self.pw = p // w   # profit per unit weight
   
   def __lt__(self, other):
      return self.pw < other.pw

def frac_greedy(p, w, m):
   assert len(p) == len(w), "Profit and weight do not have the same number of elements!"
   x = []
   n = len(p)
   item_fractions = [0] * n
   result = []

   for i in range(n):
      x.append(ItemValue(p[i], w[i], i))

   x.sort(reverse=True) # sorting items by profit
   totalProfit = 0

   for i in x:
      current_weight = int(i.w)
      current_profit = int(i.p)

      if m - current_weight >= 0:
         item_fractions[i.index] = 1
         m -= current_weight
         totalProfit += current_profit
      
      else:
         fraction = m / current_weight
         totalProfit += current_profit * fraction
         item_fractions[i.index] = fraction
         m = int(m - (current_weight * fraction)) # m = 0 (weight limit is reached)
         break 

   result.append(item_fractions)
   result.append(totalProfit)

   return result

# Solve 0/1 Knapsack problem using Dynamic Programming
def dynamic(p, w, m):
   assert len(p) == len(w), "Profit and weight do not have the same number of elements!"
   n = len(p)
   K = [[0 for x in range(m + 1)] for x in range(n + 1)] 

   # Build table K[][] in bottom up manner 
   for i in range(n + 1): 
      for j in range(m + 1): 
         if i == 0 or j == 0: 
               K[i][j] = 0

         elif w[i-1] <= j: 
               K[i][j] = max(p[i-1] + K[i-1][j-w[i-1]], K[i-1][j]) 

         else: 
               K[i][j] = K[i-1][j] 
  
   return K[n][m] 

if __name__ == '__main__':
   p = [21, 16, 27, 12]
   w = [4, 10, 13, 7]  
   m = 20

   max_profit_bruteforce = bruteforce(p, w, m)
   print("0/1 Knapsack using Bruteforce = ", max_profit_bruteforce)
'''
   max_profit_frac_bruteforce = frac_bruteforce(p, w, m)
   print("Fractional Knapsack using Bruteforce = ", max_profit_frac_bruteforce)

   max_profit_greedy = frac_greedy(p, w, m)
   print("Fractional Knapsack using Greedy algorithm = ", max_profit_greedy)

   max_profit_dynamic = dynamic(p, w, m)
   print("0/1 Knapsack using Dynamic Programming = ", max_profit_dynamic)

'''