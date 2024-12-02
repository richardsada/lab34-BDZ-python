
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных
f1 = open("Users\Семен\Documents\Python\BDZ/train.csv")
f2 = open("Users\Семен\Documents\Python\BDZ/test.csv")
train_df = pd.read_csv(f1)
test_df = pd.read_csv(f2)
#2  Вывод статистики по числовым полям, разделенной по полу
male_stats = train_df[train_df['Sex'] == 'male'].describe()
female_stats = train_df[train_df['Sex'] == 'female'].describe()

print("Статистика для мужчин:\n", male_stats)
print("\nСтатистика для женщин:\n", female_statas)