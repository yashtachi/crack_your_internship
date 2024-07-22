
from bisect import bisect_left
 
arr = [1, 2, 8, 10, 10, 12, 19]
n = len(arr)
x = 8
 
# Use bisect to get ceiling element
idx = bisect_left(arr, x)
 
# Checking if idx is valid
if idx == n:
    print("Ceil Element does not exist")
else:
    print(f"Ceil Element of {x} is {arr[idx]}")