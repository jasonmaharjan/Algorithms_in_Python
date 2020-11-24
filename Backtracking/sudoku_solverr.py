def displayGrid(grid):
   print('\n')
   for i in range(9):
      for j in range(9):
         print (grid[i][j], end = ' ')
      print('\n')

# Check if the grid is full
def checkGrid_full(grid):
  # loop through each row
  for row in range(0,9):
    # loop through every column in very row
      for col in range(0,9):
        # check if cell is empty
        if grid[row][col] == 0:
          return 0
  # Grid is complete
  return 1
 
# Grid Solver
def solveGrid(grid):
   for i in range(0,81):
      row = i // 9
      col = i % 9
      # look for empty cell to put digits(1-9)
      if grid[row][col] == 0:
         for val in range (1,10):
            # Check if digit is already used in this row
            if not(val in grid[row]):
               # Check if digit is already used in this column
               if not(val in (grid[i][col] for i in range(9))):
                  # current square (out of the 9 squares)
                  current_square = []
                  if row<3:
                     if col<3:
                        current_square=[grid[i][0:3] for i in range(0,3)]
                     elif col<6:
                        current_square=[grid[i][3:6] for i in range(0,3)]
                     else:  
                        current_square=[grid[i][6:9] for i in range(0,3)]
                  elif row<6:
                     if col<3:
                        current_square=[grid[i][0:3] for i in range(3,6)]
                     elif col<6:
                        current_square=[grid[i][3:6] for i in range(3,6)]
                     else:  
                        current_square=[grid[i][6:9] for i in range(3,6)]
                  else:
                     if col<3:
                        current_square=[grid[i][0:3] for i in range(6,9)]
                     elif col<6:
                        current_square=[grid[i][3:6] for i in range(6,9)]
                     else:  
                        current_square=[grid[i][6:9] for i in range(6,9)]

                  # Check if this value has not already been used on the 3x3 current_square
                  if not val in (current_square[0] + current_square[1] + current_square[2]):
                     grid[row][col] = val

                     # Check if grid is full
                     if checkGrid_full(grid):
                        return 1
                     else:
                        if solveGrid(grid):
                           return 1
         break
   # remove the assigned value i.e. backtracking is commenced
   grid[row][col] = 0
 
# Driver funtion
if __name__=="__main__":
   # initialize partial grid
   grid = []
   grid.append([3, 0, 6, 5, 0, 8, 4, 0, 0])
   grid.append([5, 2, 0, 0, 0, 0, 0, 0, 0])
   grid.append([0, 8, 7, 0, 0, 0, 0, 3, 1])
   grid.append([0, 0, 3, 0, 1, 0, 0, 8, 0])
   grid.append([9, 0, 0, 8, 6, 3, 0, 0, 5])
   grid.append([0, 5, 0, 0, 9, 0, 6, 0, 0])
   grid.append([1, 3, 0, 0, 0, 0, 2, 5, 0])
   grid.append([0, 0, 0, 0, 0, 0, 0, 7, 4])
   grid.append([0, 0, 5, 2, 0, 6, 3, 0, 0])     

   if(solveGrid(grid)):
      displayGrid(grid)
   else:
      print ("Solution doesn't exist for the given sudoku")