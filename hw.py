import sympy as sp

# Змінна
x = sp.symbols("x")

# Функції
f1 = x**3 / 3 + x**2 / 2 - 2 * x
f2 = sp.sqrt(x**2 + 1)
f3 = 1 / sp.sqrt(x**2 + 1)

functions = [f1, f2, f3]
names = [
    "f1(x) = x^3/3 + x^2/2 - 2x",
    "f2(x) = sqrt(x^2) + 1",
    "f3(x) = 1/sqrt(x^2 + 1)",
]

# Точки
points = [1, -sp.Rational(1, 2)]

for fname, f in zip(names, functions):
    print(f"\n{fname}")
    f_prime = sp.diff(f, x)
    print("Похідна:", f_prime)

    for p in points:
        value = f_prime.subs(x, p).evalf()
        print(f"Значення при x={p}: {value}")
