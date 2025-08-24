import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Завантаження даних
url = "https://docs.google.com/spreadsheets/d/1OPnEAT64Patnj_Ifhwn_pM1c15rsBNIoFrtz38A1_W4/export?format=csv"
df = pd.read_csv(url)

# --- 1. Перевірка пропусків ---
print("Кількість пропусків у кожній колонці:")
print(df.isnull().sum())

# --- 2. Перетворення бінарних ознак ---
binary_mappings = {
    "Furnishing Status": {"Furnished": 1, "Unfurnished": 0},
    "Tenant Preferred": {"Bachelors": 0, "Family": 1},
}

for col, mapping in binary_mappings.items():
    if col in df.columns:
        df[col] = df[col].map(mapping)

# --- 3. Статистика числових колонок ---
print("\nОписова статистика:")
print(df.describe())

print("\nДисперсія числових колонок:")
print(df.var())

print("\nСтандартне відхилення числових колонок:")
print(df.std())

# --- 4. Кореляційна матриця ---
corr_matrix = df.corr()
print("\nКореляційна матриця:")
print(corr_matrix)

# --- 5. Візуалізація ---
# Гістограми числових колонок
df.hist(figsize=(12, 10))
plt.tight_layout()
plt.show()

# Парні графіки для візуалізації залежностей
sns.pairplot(df.select_dtypes(include=["int64", "float64"]))
plt.show()
