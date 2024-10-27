import numpy as np
import matplotlib.pyplot as plt

# Определим функцию для расчета значений T(n)
def Tworst(n):
    return (n - 1) * n / 2 + (n - 1)



# Создадим массив значений n
n_values = np.arange(1, 101)  # диапазон от 1 до 100

# Рассчитаем значения для всех трех функций (они одинаковы в данном случае)
Tworst_values = T(n_values)
Taverage_values = T(n_values)
Tbest_values = T(n_values)

# Построим графики
plt.figure(figsize=(12, 6))
plt.plot(n_values, Tworst_values, label='Tworst(n)', color='red')
plt.plot(n_values, Taverage_values, label='Taverage(n)', color='green')
plt.plot(n_values, Tbest_values, label='Tbest(n)', color='blue')

# Добавим подписи и легенду
plt.title('Selection Sort')
plt.xlabel('n')
plt.ylabel('T(n)')
plt.legend()
plt.grid()

# Показать график
plt.show()

