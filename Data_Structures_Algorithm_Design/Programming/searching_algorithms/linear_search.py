# Function definition
def linear_search(arr,x):
  for i in range(len(arr)):
    if arr[i]==x:
      return i
  return -1

# Driver code
arr = [2,1,8,9,12,15,11,19]
x = 15
# Function calling
result = linear_search(arr,x)
print("Searching element is present at the index", result)
