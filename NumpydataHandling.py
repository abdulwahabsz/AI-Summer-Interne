import numpy as np

arr1= np.array([1,2,3,4,5])
print(arr1)

arr2 =np.array([[1,2,3],[4,5,6]])
print(arr2)

zeros_arr = np.zeros((2,3))
ones_arr = np.ones((2,2))
range_arr = np.arange(0,10,2)
linspace_arr = np.linspace(0,1,5)

# 1D array
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])      # First element
print(arr[-1])     # Last element
print(arr[1:4])    # Slice

# 2D array
arr2d = np.array([[10, 20, 30], [40, 50, 60]])
print(arr2d[0, 1])   # Row 0, Col 1
print(arr2d[:, 1])   # All rows, col 1
print(arr2d[1, :])   # Row 1, all cols

#ARRAY OPERATIONS
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # Element-wise add
print(a - b)   # Element-wise subtract
print(a * b)   # Element-wise multiply
print(a / b)   # Element-wise divide

# Broadcasting
m = np.array([[1], [2], [3]])
n = np.array([10, 20, 30])
print(m + n)  # Broadcast addition
