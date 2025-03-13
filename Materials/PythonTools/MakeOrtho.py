from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt

import sys

# Parse first three command line arguments as floats azimuth, theta and phi
# Parse the next three as x_scale, y_scale and z_scale.
if len(sys.argv) != 7:
    print("Usage: script.py azimuth theta phi x_scale y_scale z_scale")
    sys.exit(1)

azimuth, theta, phi = map(float, sys.argv[1:4])
x_scale, y_scale, z_scale = map(float, sys.argv[4:7])

# Create an array az_rotate that rotates the array by azimuth radans 
# about the z-axis
az_rotate = np.array([[np.cos(azimuth), -np.sin(azimuth), 0],
                      [np.sin(azimuth), np.cos(azimuth), 0],
                      [0, 0, 1]])

# Create an array theta_rotate that rotates the array by theta degrees about the y-axis
theta_rotate = np.array([[np.cos(theta), 0, np.sin(theta)],
                         [0, 1, 0],
                         [-np.sin(theta), 0, np.cos(theta)]])

# Create an array phi_rotate that rotates the array by phi radians about the x-axis
phi_rotate = np.array([[1, 0, 0],
                       [0, np.cos(phi), -np.sin(phi)],
                       [0, np.sin(phi), np.cos(phi)]])

# Create an array rot_array that is the product of az_rotate, 
# theta_rotate and phi_rotate
rot_array1 = np.matmul(theta_rotate, az_rotate)
rot_array = np.matmul(phi_rotate, rot_array1)

inv_rot_array = np.linalg.inv(rot_array)

diag_array = np.array([[x_scale, 0, 0], 
                       [0, y_scale, 0], 
                       [0, 0, z_scale]]); 

# Multiply inv_rot_array by diag_array by rot_array
result = np.matmul(np.matmul(inv_rot_array, diag_array), rot_array)
print(result)
# Compute its inverse and determinant
try:
    inverse_array = np.linalg.inv(result)
    det = np.linalg.det(result)
except np.linalg.LinAlgError:
    inverse_array = "Inverse does not exist for this array"

print(f"Original Array:\n{result}")
print(f"Inverse:\n{inverse_array}\nDeterminant: {det}")