# Sudoku solver using backtracking
# Display grid
def display_grid(grid):
    print('\n')
    for i in range(9):
        for j in range(9):
            print (grid[i][j], end = ' ')
        print('\n')

# Searches the grid to find an entry that is still unassigned. 
# If found, the reference parameters row, col will be set to the grid cell that is unassigned, and true is returned.
# If not found unassigned entries remains, false is returned.
# 'l' is a list  variable that has been passed from the solve_sudoku function to keep track of incrementation of Rows and Columns
def find_empty_cells(grid, l):
    for row in range(9):
        for col in range(9):
            if(grid[row][col] == 0):
                l[0]= row
                l[1]= col
                return 1
    return 0
 
# check if assigned entry in the specified row matches the given number
def used_in_row(grid, row, num):
    for i in range(9):
        if(grid[row][i] == num):
            return 1
    return 0
 
# check if assigned entry in the specified column matches the given number
def used_in_col(grid, col, num):
    for i in range(9):
        if(grid[i][col] == num):
            return 1
    return 0
 
# check if assigned entry within the specified 3x3 box matches the given number
def used_in_box(grid, row, col, num):
    for i in range(3):
        for j in range(3):
            if(grid[i + row][j + col] == num):
                return 1
    return 0
 
# Check if a digit can be assigned to the given row, col
def check_cell(grid, row, col, num):
    # Check if 'num' is not already placed in current row,current column and current 3x3 box
    return (not used_in_row(grid, row, num) and
           not used_in_col(grid, col, num) and
           not used_in_box(grid, row - row % 3, 
                           col - col % 3, num))
 
# Solve the partial grid fulfilling the 3 constraints
def solve_sudoku(grid):
    # 'l' is a list variable that keeps the record of row and col in find_empty_cells()
    l =[0, 0]
     
    # If there is no unassigned location, solution is attained
    if(not find_empty_cells(grid, l)):
        return 1
     
    # Assigning list values to row and col that we got from the above Function 
    row = l[0]
    col = l[1] 

    # for digits 1 to 9
    for num in range(1, 10):
        if(check_cell(grid, row, col, num)):
            # make tentative assignment
            grid[row][col]= num
            # return, if success
            if(solve_sudoku(grid)):
              return 1
 
            # failure, unmake & try again
            grid[row][col] = 0
             
    # trigger backtracking       
    return 0
 
# Driver funtion
if __name__=="__main__":
     
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
     
    if(solve_sudoku(grid)):
        display_grid(grid)
    else:
        print ("Solution doesn't exist for the given sudoku")