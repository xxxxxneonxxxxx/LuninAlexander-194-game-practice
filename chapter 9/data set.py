import pandas as pd
import numpy as np  # linear algebra
import matplotlib.pyplot as plt

# Загрузка данных и их копирование
df = (pd.read_csv('D:\\chapters\\.venv\\chapter 9\\supermarket_sales.csv'))
for i in df['Payment']:
    print(i)
df_2 = df.copy()
# Создаем таблицу сопряженности
a = pd.crosstab(df_2['Rating'], df_2['Payment'])
# Построение столбчатой диаграммы
ax =a.plot(kind='bar', stacked=False, figsize=(12, 9), color=['skyblue', 'salmon', 'lightgreen'])

# Добавление заголовка и меток осей
plt.title('Payment vs Rating')
plt.xlabel('Payment')
plt.ylabel('Rating')
plt.xticks(rotation=0)
plt.legend(title='Payment')

for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=8)

plt.tight_layout()
plt.show()
