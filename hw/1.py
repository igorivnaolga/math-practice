from itertools import product

# Генеруємо всі можливі комбінації для трьох гральних кубиків (1-6)
all_combinations = list(product(range(1, 7), repeat=3))

# Обчислюємо суму очок для кожної комбінації
sums = [sum(combo) for combo in all_combinations]

# Рахуємо ймовірності для сум 11 та 12
prob_11 = sums.count(11) / len(all_combinations)
prob_12 = sums.count(12) / len(all_combinations)

# Виводимо результати
print(f"Ймовірність, що сума очок = 11: {prob_11:.3f} ({prob_11*100:.1f}%)")
print(f"Ймовірність, що сума очок = 12: {prob_12:.3f} ({prob_12*100:.1f}%)")

# Висновок
if prob_11 > prob_12:
    print("Отримати суму 11 ймовірніше, ніж суму 12.")
elif prob_11 < prob_12:
    print("Отримати суму 12 ймовірніше, ніж суму 11.")
else:
    print("Ймовірності для сум 11 та 12 однакові.")
