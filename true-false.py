from itertools import product


# Функція імплікації
def impl(p, q):
    return (not p) or q


# Змінні A, B, C, D
variables = ["A", "B", "C", "D"]

# Заголовок таблиці
print(f"| {' | '.join(variables)} | A→(B∨C) | B∧C | (B∧C)→D | X |")
print("|" + "----|" * (len(variables) + 4))

# Генеруємо всі комбінації істинності (0 або 1)
for A, B, C, D in product([0, 1], repeat=4):
    a_imp_b_or_c = impl(A, B or C)
    b_and_c = B and C
    b_and_c_imp_d = impl(b_and_c, D)
    X = a_imp_b_or_c and b_and_c_imp_d
    print(
        f"| {A} | {B} | {C} | {D} | {a_imp_b_or_c} | {b_and_c} | {b_and_c_imp_d} | {X} |"
    )
