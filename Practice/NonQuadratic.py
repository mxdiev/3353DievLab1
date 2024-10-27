import random
import time
import numpy as np
import matplotlib.pyplot as plt

# Функция для полиномиальной регрессии и построения графика
def plot_regression(n, data, degree, label_data, label_fit, color):
    # Построение точек
    plt.plot(n, data, 'o', color=color, label=label_data)
    
    # Полиномиальная регрессия
    p = np.polyfit(n, data, degree)
    n_fit = np.linspace(n.min(), n.max(), 100)
    data_fit = np.polyval(p, n_fit)
    
    # Построение регрессионной кривой
    plt.plot(n_fit, data_fit, '-', color=color, label=label_fit)

def selection_sort(arr):
    # Реализация сортировки выбором
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    # Реализация сортировки вставками
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def merge_sort(arr):
    # Реализация сортировки слиянием
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    # Реализация быстрой сортировки
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def shell_sort_Shell(arr):
    # Реализация сортировки Шелла
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def shell_sort_Hibbard(arr):   
    n = len(arr)
    # Генерация последовательности Хиббарда
    h = 1
    hibbard_sequence = []
    while h < n:
        hibbard_sequence.append(h)
        h = 2 * h + 1  # Следующий элемент последовательности Хиббарда
    # Сортировка с использованием последовательности Хиббарда
    for gap in reversed(hibbard_sequence):  # Проходим по последовательности в обратном порядке
        for i in range(gap, n):
            # Сохраняем текущий элемент для вставки
            temp = arr[i]
            j = i
            # Сравниваем и перемещаем элементы
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]  # Перемещаем элемент
                j -= gap
            arr[j] = temp  # Вставляем элемент в нужное место
    
def pratt_sequence(n):
    steps = []
    i, j = 0, 0
    while True:
        step = (2 ** i) * (3 ** j)
        if step > n:
            break
        steps.append(step)
        if (2 ** (i + 1)) * (3 ** j) <= n:
            i += 1
        else:
            i = 0
            j += 1
    return sorted(steps, reverse=True)

def shell_sort_Pratt(arr):
    n = len(arr)
    steps = pratt_sequence(n)  # Получаем шаги по последовательности Пратта
    for step in steps:
        for i in range(step, n):
            temp = arr[i]
            j = i
            while j >= step and arr[j - step] > temp:
                arr[j] = arr[j - step]
                j -= step
            arr[j] = temp
    

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


#создание словаря функций сортировок 
sort_functions = {
    1: selection_sort,
    2: insertion_sort,
    3: bubble_sort,
    4: merge_sort,
    5: quick_sort,
    6: shell_sort_Shell,
    7: shell_sort_Hibbard,
    8: shell_sort_Pratt,
    9: heap_sort
}
title = {
    1: "Selection Sort",
    2: "Insertion Sort",
    3: "Bubble Sort",
    4: "Merge Sort",
    5: "Quick Sort",
    6: "Shell Sort for Shell Sequence",
    7: "Shell Sort for Hibbard Sequence",
    8: "Shell Sort for Pratt Sequence",
    9: "Heap Sort"
}

table = [[0.0 for j in range(6)] for i in range(10)]

#квадратичная асимптотика

for sort in [4, 5, 8, 6, 7, 9]:
    k = 0
    for n in range(0, 60000, 10000):
        arr = [random.randint(0, 999999) for i in range(n)]
        start_time = time.time()
        sort_functions[sort](arr)
        duration = (time.time() - start_time) * 1000
        table[sort][k] = float(duration)
        k+=1

n = np.array([0, 10000, 20000, 30000, 40000, 50000])
plt.figure(figsize = (10, 6))
degree = 2
table = [np.array(arr) for arr in table]

plot_regression(n, table[4], degree, "Merge Sort Data", "Merge Sort Curve", "blue")
plot_regression(n, table[5], degree, "Quick Sort Data", "Quick Sort Curve", "red")
plot_regression(n, table[6], degree, "Shell Sort (Shell) Data", "Shell Sort (Shell) Curve", "magenta")
plot_regression(n, table[7], degree, "Shell Sort (Hibbard) Data", "Shell Sort (Hibbard) Curve", "orange")
plot_regression(n, table[8], degree, "Shell Sort (Pratt) Data", "Shell Sort (Pratt) Curve", "black")
plot_regression(n, table[9], degree, "Heap Sort Data", "Heap Sort Curve", "cyan")
plt.xlabel('n')
plt.ylabel('T(n)')
plt.title("Не квадратичная асимптотика")
plt.legend()
plt.grid(True)
plt.show()
