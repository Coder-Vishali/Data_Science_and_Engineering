# Consider sorted array

# 0 1 2 3 4 5 6 7 8 9 
# 1 2 3 4 5 6 7 8 9 10

#       |      |
#     mid1    mid2
# Part 1, Part 2, Part 3

# Search space into three spaces

# mid1 = l + (r-l)//3 == 0 + 9//3 = 3
# mid2 = r - (r-l)//3 == 9 - 9//3 = 6

# Here, l = 0 and r = 9

# x = 5 -> Searching element

# Function definition
def ternary_search(arr,x):
  left = 0
  right = len(arr) - 1
  while left<=right:
    mid1 = left + (right - left)//3
    mid2 = right - (right - left)//3
    if arr[mid1]==x:
      return mid1
    if arr[mid2]==x:
      return mid2
    elif x < arr[mid1]:
      # Move to first part
      right = mid1 -1
    elif x > arr[mid2]:
      # Move to third part
      left = mid2 + 1
    else:
      # Move to second part
      left = mid1 + 1
      right = mid2 - 1
  return -1

## Driver code
arr = [1, 2, 3,4, 5, 6, 7, 8, 9, 10]
x = 8
# Function calling
result = ternary_search(arr, x)
print("Searching element is present at index: ", result)
