import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import shapiro

# Параметри
shape, scale = 0.3, 1.1
n = 100  # кількість симуляцій
t_max = 60  # максимальний час
step = 2  # крок

# (а) Одна симуляція для x
samples = np.random.gamma(shape=shape, scale=scale, size=n)
plt.hist(samples, bins=15, edgecolor="black")
plt.title("Гістограма розподілу x (Γ(0.3, 1.1))")
plt.show()

# (б) Генерація матриці розміром (n, t_max)
data = np.random.gamma(shape=shape, scale=scale, size=(n, t_max))

# Для кожного t = 1, 3, 5, ... 60 обчислюємо суми по рядках
for t in range(1, t_max + 1, step):
    final_prices = data[:, :t].sum(axis=1)  # підсумок перших t стовпців
    stat, p_value = shapiro(final_prices)

    plt.hist(final_prices, bins=15, edgecolor="black")
    plt.title(f"t={t}, p={p_value:.3f}")
    plt.show()

    print(f"t={t}: середня ціна = {final_prices.mean():.2f}, p={p_value:.3f}")


# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import shapiro

# # Параметри гамма-розподілу
# shape = 0.3  # параметр форми
# scale = 1.1  # параметр масштабу
# n = 100  # кількість симуляцій

# # (а) Гістограма розподілу x
# samples = np.random.gamma(shape=shape, scale=scale, size=n)
# plt.hist(samples, bins=15, edgecolor="black", alpha=0.7)
# plt.title("Гістограма зміни ціни (x ~ Γ(0.3, 1.1))")
# plt.xlabel("Зміна ціни (x)")
# plt.ylabel("Частота")
# plt.grid(axis="y", alpha=0.6)
# plt.show()

# # (б) Симуляція для різних t
# t_values = range(1, 61, 2)  # від 1 до 60 з кроком 2

# for t in t_values:
#     final_prices = []
#     for _ in range(n):
#         changes = np.random.gamma(shape=shape, scale=scale, size=t)
#         final_price = np.sum(changes)
#         final_prices.append(final_price)

#     # Тест Шапіро-Уїлка на нормальність
#     stat, p_value = shapiro(final_prices)

#     # Гістограма для цього t
#     plt.hist(final_prices, bins=15, edgecolor="black", alpha=0.7)
#     plt.title(f"Гістограма ціни після t={t}, p={p_value:.3f}")
#     plt.xlabel("Кінцева ціна")
#     plt.ylabel("Частота")
#     plt.grid(axis="y", alpha=0.6)
#     plt.show()

#     print(f"t={t}: середня ціна = {np.mean(final_prices):.2f}, p={p_value:.3f}")
