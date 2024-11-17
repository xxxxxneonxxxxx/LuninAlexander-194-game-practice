import pandas as pd
import numpy as np  # linear algebra
import matplotlib.pyplot as plt
import datetime
y1,y2,y3,y4=set(),set(),set(),set()
# Загрузка данных и их копирование
df = (pd.read_csv('D:\\chapters\\.venv\\chapter 9\\supermarket_sales.csv'))
'Date,Quantity,gross income'
g=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df_2 = df.copy()

for i in df['Date']:
    i1=str(i).split("/")
    i1=datetime.datetime(int(i1[2]),int(i1[0]),int(i1[1]))
    i1=g[i1.weekday()]
    df_2['Date'] = df_2['Date'].replace(i,i1)
# Создаем таблицу сопряженности
a = pd.crosstab(df_2['Date'], ['gross income'])
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