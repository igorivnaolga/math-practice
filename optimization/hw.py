import time
from scipy.optimize import linprog

start = time.time()

# x1— сайти, x2— інтернет-магазини, x3— ERP-інтеграції.

# 2*x1 + 9*x2  + 6*x3  c

# Define the constraints
# 12*x1 + 6*x2 + 2*x3 <=320
# 12*x1 + 24*x2 + 18*x3 <= 192
# 12x1 + 18*x2 + 12*x3 <= 180
# x1, x2, x3 >= 0

# Цільова функція (мінус для максимізації)
c = [-2, -9, -6]

# Матриця обмежень (A_ub)
A_ub = [
    [12, 6, 2],
    [12, 24, 18],
    [12, 18, 12],
]

# Вектори правих частин (b_ub)
b_ub = [320, 192, 180]

bounds = [
    [0, float("inf")],  # Bounds of x1
    [0, float("inf")],  # Bounds of x2
    [0, float("inf")],
]  # Bounds of x3


# Виклик оптимізації
res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)

stop = time.time()

print(res)
print("Час виконання:", stop - start)
