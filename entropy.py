import collections
import math


def calculate_entropy(text):
    # Підрахунок кількості входжень кожного символу у тексті
    frequencies = collections.Counter(text)

    # Загальна кількість символів у тексті
    total_characters = len(text)

    # Обчислення ентропії за формулою
    entropy = -sum(
        (count / total_characters) * math.log2(count / total_characters)
        for count in frequencies.values()
    )

    return entropy


# Приклад використання
text_example = "aaaabbcd"
entropy_value = calculate_entropy(text_example)
print(f"Ентропія тексту: {entropy_value} біт")
