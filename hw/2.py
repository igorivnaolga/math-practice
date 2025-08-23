import numpy as np
import matplotlib.pyplot as plt

# Параметри
steps = 3
increments = [2, -1]
probabilities = [0.5, 0.5]
simulations_list = [10, 100, 1000, 10000]

# Симуляція та візуалізація
for n_sim in simulations_list:
    final_prices = []
    for _ in range(n_sim):
        changes = np.random.choice(increments, size=steps, p=probabilities)
        final_price = np.sum(changes)
        final_prices.append(final_price)
    mean_price = np.mean(final_prices)
    print(f"{n_sim} симуляцій: середня ціна = {mean_price:.3f}")

    plt.figure()
    plt.hist(
        final_prices,
        bins=range(min(final_prices), max(final_prices) + 2),
        edgecolor="black",
        align="left",
    )
    plt.title(f"Гістограма кінцевих цін (N={n_sim})")
    plt.xlabel("Ціна")
    plt.ylabel("Частота")
    plt.grid(axis="y", alpha=0.7)
    plt.show()
