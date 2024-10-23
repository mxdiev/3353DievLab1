import random
import time

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

def main():

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

    while True:
        print("Выберите сортировку:")
        print("1. Сортировка выбором (Selection Sort)")
        print("2. Сортировка вставками (Insertion Sort)")
        print("3. Сортировка пузырьком (Bubble Sort)")
        print("4. Сортировка слиянием (Merge Sort)")
        print("5. Быстрая сортировка (Quick Sort)")
        print("6. Сортировка Шелла для последовательности Шелла (Shellsort)")
        print("7. Сортировка Шелла для последовательности Хиббарда (Shellsort)")
        print("8. Сортировка Шелла для последовательности Пратта (Shellsort)")
        print("9. Пирамидальная сортировка (Heap sort)")

        kEx, kIn = 0, 0
        table = [[0.0 for j in range(6)] for i in range(4)]
        narray = []
        #print(table)

        menu = int(input("Выбор: "))
        for size in range(0, 30000, 5000):
            kIn = 0
            ASorted = list(range(size))
            ARandom = [random.randint(0, 999999) for _ in range(size)]
            ANotSorted = list(range(size, 0, -1))  
            ANearlySorted = list(range(int(0.9 * size))) + [random.randint(0, 999999) for _ in range(size - int(0.9 * size))]
            if menu in sort_functions:
                for arr, name in zip(
                    [ASorted.copy(), ANearlySorted.copy(), ARandom.copy(), ANotSorted.copy()],
                    ["отсортированного", "частично отсортированного (90/10)", "случайных чисел", "в обратном порядке"]
                ):
                    start_time = time.time()
                    sort_functions[menu](arr)
                    duration = (time.time() - start_time) * 1000
                    table[kIn][kEx] = float(duration)
                    kIn+=1
                    print(f"Время обработки массива {name} при n = {size}: {duration:.2f} мс.")
            else:
                print("Некорректный выбор. Попробуйте снова.")
            print()
            kEx+=1
            narray.append(size)
        print(table)
            
        table = [[round(x, 2) for x in table[i]] for i in range(4)]
        for i in range(len(table)):
            s = ""
            for j in range(len(table[i])):
                s += str(table[i][j]) + "\t"
            print(s)
        print("ASorted = " + str(table[0]))
        print("ANearlySorted = " + str(table[1]))
        print("ARandom = " + str(table[2]))
        print("ANotSorted = " + str(table[3]))
        print("n = " + str(narray))

    
if __name__ == "__main__":
    main()
