# Import NumPy as np
import numpy as np

# Create an array of 10 zeros
print(np.zeros(10))

# Create an array of 10 ones
print(np.ones(10))

# Create an array of 10 fives
print(5*np.ones(10))

# Create an array of the integers from 10 to 50
print(np.arange(10, 51))

# Create an array of all the even integers from 10 to 50
print(np.arange(10, 51, 2))

# Create a 3x3 matrix with values ranging from 0 to 8
arr = np.arange(9).reshape(3, 3)
print(arr)

# Create a 10x10 matrix from 0.01 - 1
arr = np.arange(1, 101).reshape(10, 10)/100
print(arr)

# Create an array of 20 linearly spaced points between 0 and 1:
arr = np.linspace(0, 1, 20)
print(arr)

# replicate
# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])

arr = np.arange(1, 26).reshape(5, 5)
print(arr)

# array([[12, 13, 14, 15],
#        [17, 18, 19, 20],
#        [22, 23, 24, 25]])
arr1 = np.arange(12, 16)
arr2 = np.arange(17, 21)
arr3 = np.arange(22, 26)
arr = np.concatenate((arr1, arr2, arr3)).reshape(3, 4)
print(arr)

# array([[ 2],
#        [ 7],
#        [12]])

arr = np.arange(2, 13, 5).reshape(3, 1)
print(arr)

# array([21, 22, 23, 24, 25])
arr = np.arange(21, 26)
print(arr)

# array([[16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])
arr = np.arange(16, 26).reshape(2, 5)
print(arr)

# Create a 3x3 identity matrix
arr = np.eye(3)
print(arr)

# Use NumPy to generate a random number between 0 and 1
arr = np.random.rand(1)
print(arr)

# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
arr = np.random.randn(25)
print(arr)

# Get the sum of all the values in mat
mat = np.arange(1, 26).reshape(5, 5)
print(mat.sum())

# Get the standard deviation of the values in mat
print(mat.std())

# array([55, 60, 65, 70, 75])
print(sum(mat))
# or
print(mat.sum(axis=0))
