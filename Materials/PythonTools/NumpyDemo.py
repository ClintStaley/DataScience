import numpy as np
import matplotlib.pyplot as plt

# 1. Create NumPy arrays of various shapes
arr_1d = np.array([1, 2, 3])
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])
arr_3d = np.arange(24).reshape((2, 3, 4))  # 3D array with shape (2, 3, 4)

print("1D Array:\n", arr_1d)
print("2D Array:\n", arr_2d)
print("3D Array:\n", arr_3d)

# 2. Demonstrate broadcasting
# Adding a 1D array to each row of a 2D array
broadcast_result = arr_2d + arr_1d
print("Broadcasted Addition Result:\n", broadcast_result)

# 3. Simple linear algebra: matrix multiplication
# (2x3) dot (3x2) to get a (2x2) matrix
mat_a = np.array([[1, 2, 3],
                  [4, 5, 6]])
mat_b = np.array([[7, 8],
                  [9, 10],
                  [11, 12]])
product = mat_a.dot(mat_b)
print("Matrix Multiplication (mat_a x mat_b):\n", product)

# 4. Save and load arrays to/from text files
# Save arr_2d to output.txt
np.savetxt("output.txt", arr_2d, fmt="%d")
# In practice, you'd create or have an existing file "input.txt"
# For demonstration, we assume it exists and contains data with correct shape
# loaded_arr = np.loadtxt("input.txt")

# 5. Use matplotlib to display a NumPy array
# We'll display arr_2d as an image for illustration
plt.imshow(arr_2d, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Value Scale')
plt.title("arr_2d Visualization")
plt.show()
