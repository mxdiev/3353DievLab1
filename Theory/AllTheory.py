import numpy as np
import matplotlib.pyplot as plt

def Tselection(n):
    return (n - 1) * n / 2 + (n - 1)

def Tinsertion(n):
    return n*(n-1)/4

def Tbubble(n):
    return 3*n*(n-1)/4

def Tmerge(n):
    return n + n*np.log2(n)

def Tquick(n):
    return 2*(n+1)*np.log2(n)

def Tshell(n):
    return n**(1.5)

def Thibbard(n):
    return 2*(n+1)*np.log2(n)

def Tpratt(n):
    return n*((np.log2(n))**2)

def Theap(n):
    return (n/2) * (11 + np.log2(n)/2) + (n - 1)*np.log2(n)

# Создадим массив значений n
n_values = np.arange(1, 101)  # диапазон от 1 до 100

# Рассчитаем значения для всех трех функций (они одинаковы в данном случае)
Tselection_values = Tselection(n_values)
Tinsertion_values = Tinsertion(n_values)
Tbubble_values = Tbubble(n_values)
Tmerge_values = Tmerge(n_values)
Tshell_values = Tshell(n_values)
Thibbard_values = Thibbard(n_values)
Tpratt_values = Tpratt(n_values)
Tquick_values = Tquick(n_values)
Theap_values = Theap(n_values)

# Построим графики
plt.figure(figsize=(12, 6))
plt.plot(n_values, Tselection_values, label='Selection Sort', color='red')
plt.plot(n_values, Tinsertion_values, label='Insertion Sort', color='green')
plt.plot(n_values, Tbubble_values, label='Bubble Sort', color='cyan')
plt.plot(n_values, Tquick_values, label='Quick Sort', color='black')
plt.plot(n_values, Tmerge_values, label='Merge Sort', color='blue')
plt.plot(n_values, Tshell_values, label='Shell Sort for Shell Sequence', color='magenta')
plt.plot(n_values, Thibbard_values, label='Shell Sort for Hibbard Sequence', color='pink')
plt.plot(n_values, Tpratt_values, label='Shell Sort for Pratt Sequence', color='orange')
plt.plot(n_values, Theap_values, label='Heap Sort for Pratt Sequence', color='orange')


# Добавим подписи и легенду
plt.title('Taverage(n)')
plt.xlabel('n')
plt.ylabel('T(n)')
plt.legend()
plt.grid()

# Показать график
plt.show()
