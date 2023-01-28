# Rowwise sorted from left to right
# First integer of each row > Last integer of the previous row

# 2D Matrix
#[1,3,5,7]
#[10,11,16,20]
#[23,30,34,60]

# m = Rows
# n = columns

# Here m = 3 and n = 4
# Total elements = n * m = 3*4 = 12

# Suppose our target is to find 3, it should return true and if the target is 22, then return false

# Now, we will implement Brute Force Approach: Time complexity is O (m*n)

def solution1(arr,m,n,target):
  for i in range(m):
    for j in range(n):
      if arr[i][j]==target:
        return true
  return false
    
# As the time complexity is high, we need to go for different approach:
# Consider the matrix as row major form  -> Virutal array

# 0 1 2 3 4  5  6  7  8  9  10 11 ---> Index
# 1 3 5 7 10 11 16 20 23 30 34 60 ----> Value

# Now, we will apply binary search

# Function definition
def searchSortedMatrix(matrix, target):
  # number of rows
  m = len(matrix)
  if m == 0:
    return False
  # number of columns
  n = len(matrix[0])
  
  # Binary search implementation
  left, right = 0, m*n-1
  while left <= right:
    mid = left + (right-left)//2
    ## Extracting the elements from the 2D array
    # row_number = idx //n
    # col_number = idx % n
    mid_element = matrix[mid//n][mid%n]
    if mid_element == target:
      return True
    elif mid_element > target:
      # Move left
      right = mid -1
    else:
      left = mid + 1
  return False

## Driver code
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
## Function calling
result = searchSortedMatrix(matrix, target)
print(result)
