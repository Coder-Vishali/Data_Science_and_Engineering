# Function Definition
def binary_search(arr, i, j):
  while i<=j:
      mid =i + (j-i)//2
      if arr[mid]!='inf':
          # Move to the right part
          i = mid + 1
      if arr[mid] == 'inf':
        # Check for the previous value, if it's not infinity, then return the index
        if arr[mid-1]!='inf':
          return mid
        else:
          # Move to the left part
          j = mid - 1
  else:
      return -1

# Driver code
## Sorted array
arr = [2,1,8,9,12,15,11,'inf','inf','inf']
# Function calling
result = binary_search(arr, 0, len(arr) -1)
print("Searching element is present at the index", result)
