import numpy as np
import matplotlib.pyplot as plt

# Определим функцию для расчета значений T(n)
def Tworst(n):
    return n*(n-1)

def Tbest(n):
    return n - 1

def Taverage(n):
    return 3*n*(n-1)/4


# Создадим массив значений n
n_values = np.arange(1, 101)  # диапазон от 1 до 100

# Рассчитаем значения для всех трех функций (они одинаковы в данном случае)
Tworst_values = Tworst(n_values)
Taverage_values = Taverage(n_values)
Tbest_values = Tbest(n_values)

# Построим графики
plt.figure(figsize=(12, 6))
plt.plot(n_values, Tworst_values, label='Tworst(n)', color='red')
plt.plot(n_values, Taverage_values, label='Taverage(n)', color='black')
plt.plot(n_values, Tbest_values, label='Tbest(n)', color='blue')

# Добавим подписи и легенду
plt.title('Bubble Sort')
plt.xlabel('n')
plt.ylabel('T(n)')
plt.legend()
plt.grid()

# Показать график
plt.show()

