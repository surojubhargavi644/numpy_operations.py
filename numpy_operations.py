import numpy as np
import time
# 1D Array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# 2D Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)

# 3D Array
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array:\n", arr3)
print("\nAddition:", arr1 + 5)
print("Multiplication:", arr1 * 2)
print("Square:", arr1 ** 2)
print("Square Root:", np.sqrt(arr1))
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])

result = matrix + vector
print("\nBroadcasting Result:\n", result)
data = np.array([10, 20, 30, 40, 50])

print("\nMean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Sum:", np.sum(data))
print("Max:", np.max(data))
print("Min:", np.min(data))
# Python List
start = time.time()
py_list = list(range(1000000))
py_result = [x * 2 for x in py_list]
end = time.time()
print("\nPython List Time:", end - start)

# NumPy Array
start = time.time()
np_array = np.arange(1000000)
np_result = np_array * 2
end = time.time()
print("NumPy Array Time:", end - start)
random_array = np.random.rand(3, 3)
print("\nRandom 3x3 Array:\n", random_array)

random_integers = np.random.randint(1, 100, size=(5,))
print("Random Integers:", random_integers)
# Without NumPy (loop)
start = time.time()
total = 0
for i in range(1000000):
    total += i
end = time.time()
print("\nLoop Sum Time:", end - start)

# With NumPy
start = time.time()
total_np = np.sum(np.arange(1000000))
end = time.time()
print("NumPy Sum Time:", end - start)
print("\nArray Shape:", arr2.shape)
print("Array Dimensions:", arr2.ndim)
print("Array Size:", arr2.size)
print("Data Type:", arr2.dtype)
