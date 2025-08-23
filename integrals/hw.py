import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# змінна
x = sp.Symbol("x", real=True)

# функція f(x)
f = 2 * (
    (4 / (1.2 * sp.sqrt(2 * sp.pi))) * sp.exp(-0.5 * ((x - 11) / 1.2) ** 2)
    + (7 / (2.4 * sp.sqrt(2 * sp.pi))) * sp.exp(-0.5 * ((x - 15) / 2.4) ** 2)
)

# Невизначений інтеграл
F = sp.integrate(f, x)
print("Невизначений інтеграл f(x) dx:")
print(F.simplify())

# Визначений інтеграл від a=9 до b=18
a, b = 9, 18
I_ab = sp.integrate(f, (x, a, b))
print(f"\nКількість тасків з {a} до {b}: {I_ab.evalf()}")

# --- Візуалізація ---
f_num = sp.lambdify(x, f, "numpy")

X = np.linspace(0, 24, 500)
Y = f_num(X)

plt.figure(figsize=(10, 5))
plt.plot(X, Y, label="Ефективність f(x)")
plt.axvline(a, color="red", linestyle="--", label="Початок робочого дня (9)")
plt.axvline(b, color="green", linestyle="--", label="Кінець робочого дня (18)")
plt.fill_between(
    X, Y, where=(X >= a) & (X <= b), alpha=0.3, color="orange", label="Робочий час"
)
plt.xlabel("Години доби (x)")
plt.ylabel("Кількість тасків за одиницю часу")
plt.title("Ефективність роботи співробітників протягом доби")
plt.legend()
plt.grid()
plt.show()


def rectangle_method(f, a, b, n):
    h = (b - a) / n
    result = 0
    for i in range(1, n + 1):
        xi = a + i * h
        result += f(xi - h / 2)
    return h * result


I_rect = rectangle_method(f_num, a, b, n=1000)
print("Метод прямокутників:", I_rect)


def trapezoid_method(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        xi = a + i * h
        result += f(xi)
    return h * result


I_trap = trapezoid_method(f_num, a, b, n=1000)
print("Метод трапецій:", I_trap)


def simpson_method(f, a, b, n):
    if n % 2 == 1:  # n має бути парним
        n += 1
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        xi = a + i * h
        result += (4 if i % 2 == 1 else 2) * f(xi)
    return result * h / 3


I_simp = simpson_method(f_num, a, b, n=1000)
print("Метод Сімпсона:", I_simp)


from scipy.integrate import quad

I_quad, err = quad(f_num, a, b)
print("SciPy quad:", I_quad, " похибка:", err)
