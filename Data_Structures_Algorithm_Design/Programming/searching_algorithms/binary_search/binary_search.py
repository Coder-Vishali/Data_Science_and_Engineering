# Function definition
def binary_search(arr, i, j, x):
  while i<=j:
      mid =i + (j-i)//2
      if arr[mid]==x:
          return mid
      elif arr[mid] > x:
          j = mid-1
      else:
          i = mid+1
  else:
      return -1

# Driver code
## Sorted array
arr = [2,1,8,9,12,15,11,19]
x = 15
# Function calling
result = binary_search(arr, 0, len(arr) -1, x)
print("Searching element is present at the index", result)
