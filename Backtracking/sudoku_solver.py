# Solve Sudoku using Backtracking
import turtle
from time import sleep

#initialise sodoku board
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

# Draw board on the screen
myPen = turtle.Turtle()
myPen.hideturtle()
myPen.tracer(0)
myPen.speed(0)
myPen.pencolor("green")
myPen.fillcolor("black")
topLeft_x = -150
topLeft_y = 150

# Draw text on the screen
def text(message,x,y,size):
    myPen.penup()
    myPen.goto(x,y)    		  
    myPen.write(message, align="left", font = ('Comic Sans MS', size, 'normal'))

# Draw grid on the screen
def drawGrid(grid):
  intDim = 35
  for row in range(0,10):
    if (row%3)==0:
      myPen.pensize(3)
    else:
      myPen.pensize(1)
    myPen.penup()
    myPen.goto(topLeft_x,topLeft_y-row*intDim)
    myPen.pendown()
    myPen.goto(topLeft_x+9*intDim,topLeft_y-row*intDim)
  for col in range(0,10):
    if (col%3)==0:
      myPen.pensize(3)
    else:
      myPen.pensize(1)    
    myPen.penup()
    myPen.goto(topLeft_x+col*intDim,topLeft_y)
    myPen.pendown()
    myPen.goto(topLeft_x+col*intDim,topLeft_y-9*intDim)

  for row in range (0,9):
      for col in range (0,9):
        # draw text of non zero cells
        if grid[row][col]!=0:
          text(grid[row][col], topLeft_x+col*intDim+9, topLeft_y-row*intDim-intDim+8, 15)


# Check if the grid is full
def checkGrid(grid):
  for row in range(0,9):
      for col in range(0,9):
        # check if cell is empty 
        if grid[row][col] == 0:
          return False

  # no empty cells
  return True 

# Backtracking Algorithm
def solveGrid(grid):
  # Find and fill empty cells
  for i in range(0,81):
    row = i // 9
    col = i % 9
    if grid[row][col] == 0:
      for value in range (1,10):
        # Check if value already exists in this row
        if not(value in grid[row]):
          # Check if value already exists in this column
          if not value in (grid[i][col] for i in range(0,9)):
            # current square
            square=[]
            if row<3:
              if col<3:
                square=[grid[i][0:3] for i in range(0,3)]
              elif col<6:
                square=[grid[i][3:6] for i in range(0,3)]
              else:  
                square=[grid[i][6:9] for i in range(0,3)]
            elif row<6:
              if col<3:
                square=[grid[i][0:3] for i in range(3,6)]
              elif col<6:
                square=[grid[i][3:6] for i in range(3,6)]
              else:  
                square=[grid[i][6:9] for i in range(3,6)]
            else:
              if col<3:
                square=[grid[i][0:3] for i in range(6,9)]
              elif col<6:
                square=[grid[i][3:6] for i in range(6,9)]
              else:  
                square=[grid[i][6:9] for i in range(6,9)]
                
            # Check if value isn't already used on this 3x3 square
            if not value in (square[0] + square[1] + square[2]):
              grid[row][col] = value # place the value in the current cell
              myPen.clear() # erase previous values
              drawGrid(grid) 
              myPen.getscreen().update()     
              
              # Check if grid is completed and checked
              if checkGrid(grid):
                print("Grid Complete and Checked")
                return True
              else:
                if solveGrid(grid):
                  return True
      break
  grid[row][col] = 0
  
  
drawGrid(grid) 
myPen.getscreen().update()
sleep(1)

solved = solveGrid(grid)
if solved:
  print("Sudoku Solved")
  text("Sudoku Solved",-60,-190,15)
else:  
  print("Cannot Solve Sudoku Grid")
  text("Cannot Solve Sudoku Grid",-130,-190,20)

myPen.getscreen().update()	