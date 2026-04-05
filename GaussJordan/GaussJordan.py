import math

# number of equations
ne = 4

# augmented matrix [A|b]
A = [
    [57.0, -24.0, 12.0, -77.0 , 102.0],
    [10.0, 33.0, 6.0, -54.0 , 47.0],
    [-7.0, 0, 30.0, 12.0 , -119.0],
    [97.0, -20.0, 91.0, -77.0 , 100.0],
    
]

# =========================
# Gauss-Jordan
# =========================
for k in range(ne):
    # Normalize the line k (pivot = 1)
    piv = A[k][k]
    for j in range(ne + 1):
        A[k][j] /= piv

    # zeroes out the other lines.
    for i in range(ne):
        if i != k:
            m = A[i][k]
            for j in range(ne + 1):
                A[i][j] -= m * A[k][j]

# =========================
# Result 
# =========================
for i in range(ne):
    print(f"x{i+1} = {A[i][ne]:.12f}")