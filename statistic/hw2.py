import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro

# Завантаження даних
url = "https://docs.google.com/spreadsheets/d/18WCpPS96Tb3cB0FCsIA92PEhcmBkp08sjYhS9DsQfJE/edit#gid=954244094"
url = url[: url.find("/edit")] + "/export?format=csv"
df = pd.read_csv(url)

# Перегляд перших рядків
print(df.head())

# Статистика для кожного стовпця
for col in df.columns:
    print(f"\nСтовпець: {col}")
    mean_val = df[col].mean()
    var_val = df[col].var()
    std_val = df[col].std()
    print(
        f"Середнє: {mean_val:.2f}, Дисперсія: {var_val:.2f}, Стандартне відхилення: {std_val:.2f}"
    )

    # Гістограма
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], kde=True, bins=15)
    plt.title(f"Гістограма {col}")
    plt.show()

    # Перевірка на нормальність (Shapiro-Wilk test)
    stat, p = shapiro(df[col])
    print(f"p-значення: {p:.6f}")
    if p > 0.05:
        print("Розподіл приблизно нормальний")
    else:
        print("Розподіл не нормальний")

# Кореляція з Product_Sold
correlations = df.corr()["Product_Sold"].sort_values(ascending=False)
print("\nКореляція з Product_Sold:")
for col, val in correlations.items():
    print(f"{col}: {val:.6f}")
