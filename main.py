import replit
import time

def printMatrix(matrix):
  for i in range(len(matrix)):
    print(matrix[i][0:])
  print("\n")
  
#----------------------------------------------------------------------------------

def printMatrixAnimation(matrix, coins):
  for i in range(len(coins)):
    print(coins[i][0:])
  print("\n")
  
  for i in range(len(matrix)):
    print(matrix[i][0:])
  time.sleep(4)
  replit.clear()

#----------------------------------------------------------------------------------

def RobotCoinCollection(C):
  row = len(C)
  col = len(C[0])
  F = [['-' for x in range(col)] for y in range(row)]
  
  F[0][0] = C[0][0]
  printMatrix(F)
  
  for j in range(1, col):
    F[0][j] = F[0][j-1] + C[0][j]
    printMatrix(F)
  
  for i in range(1, row):
    F[i][0] = F[i-1][0] + C[i][0]
    printMatrix(F)
    for j in range(1, col):
      F[i][j] = max(F[i-1][j], F[i][j-1]) +C[i][j]
      printMatrix(F)
  
  return F[row-1][col-1]

#----------------------------------------------------------------------------------

def RobotCoinCollectionAnimation(C):
  row = len(C)
  col = len(C[0])
  F = [['-' for x in range(col)] for y in range(row)]
  
  F[0][0] = C[0][0]
  printMatrixAnimation(F, C)
  
  for j in range(1, col):
    F[0][j] = F[0][j-1] + C[0][j]
    printMatrixAnimation(F, C)
  
  for i in range(1, row):
    F[i][0] = F[i-1][0] + C[i][0]
    printMatrixAnimation(F, C)
    for j in range(1, col):
      F[i][j] = max(F[i-1][j], F[i][j-1]) +C[i][j]
      printMatrixAnimation(F, C)
  
  return F[row-1][col-1]

# Data ----------------------------------------------------------------------------------

C1 = [ [ 0 , 0 , 0 , 0 , 1 , 0 ], 
       [ 0 , 1 , 0 , 1 , 0 , 0 ], 
       [ 0 , 0 , 0 , 1 , 0 , 1 ], 
       [ 0 , 0 , 1 , 0 , 0 , 1 ], 
       [ 1 , 0 , 0 , 0 , 1 , 0 ] ]

C2 = [ [ 1 , 1 , 0 , 0 , 1 , 0 ], 
       [ 0 , 0 , 0 , 1 , 0 , 0 ], 
       [ 1 , 0 , 0 , 0 , 0 , 0 ], 
       [ 0 , 1 , 1 , 0 , 0 , 1 ], 
       [ 0 , 0 , 0 , 1 , 0 , 0 ] ]

C3 = [ [ 0 , 0 , 0 , 0 , 1 , 1 ], 
       [ 0 , 0 , 0 , 0 , 0 , 0 ], 
       [ 0 , 1 , 0 , 0 , 0 , 0 ], 
       [ 0 , 0 , 0 , 1 , 0 , 1 ], 
       [ 1 , 0 , 0 , 0 , 0 , 0 ] ]

C4 = [ [ 0 , 1 , 0 , 0 , 1 , 1 , 0 ], 
       [ 0 , 0 , 0 , 1 , 0 , 0 , 1 ], 
       [ 1 , 1 , 1 , 0 , 0 , 0 , 1 ], 
       [ 0 , 1 , 0 , 0 , 1 , 1 , 0 ], 
       [ 1 , 0 , 0 , 0 , 0 , 0 , 0 ],
       [ 0 , 1 , 0 , 1 , 1 , 0 , 1 ],
       [ 1 , 1 , 0 , 0 , 0 , 1 , 1 ],
       [ 0 , 0 , 0 , 1 , 0 , 0 , 0 ]]

maxCoins = RobotCoinCollection(C4)
print("Largest amount of coins: ", maxCoins)
"""
maxCoins = RobotCoinCollectionAnimation(C3)
print("Largest amount of coins: ", maxCoins)"""
