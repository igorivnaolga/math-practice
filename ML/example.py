# Під'єднуємось до гугл диску
# from google.colab import drive

# drive.mount("/content/drive")
import pandas as pd

# шлях до датасету з даними про будинки Мельбурну
melbourne_file_path = "C:/Users/igori/Downloads/melb_data.csv"


# Створи об'єкт, який міститиме в собі наш датасет
melbourne_data = pd.read_csv(melbourne_file_path)

melbourne_data.describe()  # На виході отримуємо базові статистичні дані:


# count - кількість даних
# mean - середнє арифметичне
# std - стандартне відхилення

melbourne_data.head(10)
melbourne_data.Rooms
