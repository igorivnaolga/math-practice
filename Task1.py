import numpy as np

# Define vectors
a = np.array([1, 1 / 3, 0])
b = np.array([0, 2, 1 / 4])
c = np.array([1 / 2, 1 / 2, 1])

# Compute volume (determinant)
V = np.linalg.det(np.column_stack((a, b, c)))
print("Volume V =", V)


# Function to compute angle between two vectors
def angle_between(u, v):
    cos_theta = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
    return np.arccos(cos_theta)  # in radians


# Compute angles
angle_ab = np.degrees(angle_between(a, b))
angle_ac = np.degrees(angle_between(a, c))
angle_bc = np.degrees(angle_between(b, c))
print(f"Angle(a, b) = {angle_ab:.2f}°")
print(f"Angle(a, c) = {angle_ac:.2f}°")
print(f"Angle(b, c) = {angle_bc:.2f}°")

# Compute cross products and surface area
cross_ab = np.cross(a, b)
cross_ac = np.cross(a, c)
cross_bc = np.cross(b, c)

S = 2 * (np.linalg.norm(cross_ab) + np.linalg.norm(cross_ac) + np.linalg.norm(cross_bc))
print("Surface area S =", S)

# Compute remaining vertices assuming M0 at origin
M0 = np.array([0, 0, 0])
M1 = M0 + a
M2 = M0 + b
M3 = M0 + c
M4 = M0 + b + c
M5 = M0 + a + c
M6 = M0 + a + b
M7 = M0 + a + b + c

print("Vertices coordinates:")
print("M0 =", M0)
print("M1 =", M1)
print("M2 =", M2)
print("M3 =", M3)
print("M4 =", M4)
print("M5 =", M5)
print("M6 =", M6)
print("M7 =", M7)
