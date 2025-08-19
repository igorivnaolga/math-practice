import numpy as np
import matplotlib.pyplot as plt


# функція та її похідна
def f(x):
    return -3 * x**2 + 30 * x


def f_prime(x):
    return -6 * x + 30


# точки для графіка
x = np.linspace(0, 10, 400)
y = f(x)
y_prime = f_prime(x)

# максимум
x_max = 5
y_max = f(x_max)

# малювання
plt.figure(figsize=(10, 6))

# графік функції
plt.plot(x, y, label="y = -3x² + 30x", color="blue")
# графік похідної
plt.plot(x, y_prime, label="y' = -6x + 30", color="green", linestyle="--")
# точка максимуму
plt.scatter(x_max, y_max, color="red", s=100, zorder=5, label=f"Max (5, 75)")

plt.title("Функція, її похідна та точка максимуму")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
