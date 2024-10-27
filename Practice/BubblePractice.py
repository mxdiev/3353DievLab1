import numpy as np
import matplotlib.pyplot as plt

# Данные
ASorted = [0.0, 0.0, 1.0, 0.0, 1.0, 1.0]
ANearlySorted = [0.0, 675.69, 2727.82, 6491.97, 11129.22, 17506.31]
ARandom = [0.0, 1860.55, 7523.82, 17247.22, 30512.25, 47480.74]
ANotSorted = [0.0, 2962.13, 11920.77, 26704.86, 47394.69, 74641.86]
n = [0, 5000, 10000, 15000, 20000, 25000]

n = np.array(n)
ASorted = np.array(ASorted)
ANearlySorted = np.array(ANearlySorted)
ARandom = np.array(ARandom)
ANotSorted = np.array(ANotSorted)

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

# Построение графиков
plt.figure(figsize=(10, 6))

# Регрессия и график для каждого набора данных
degree = 2 # Степень полинома (квадратичная регрессия)

plot_regression(n, ASorted, degree, 'Sorted Data', 'Sorted Curve', 'blue')
plot_regression(n, ANearlySorted, degree, 'Nearly Sorted Data', 'Nearly Sorted Curve', 'green')
plot_regression(n, ARandom, degree, 'Random Data', 'Random Sorted Curve', 'magenta')
plot_regression(n, ANotSorted, degree, 'Reverse Sorted Data', 'Reverse Sorted Curve', 'cyan')

# Настройка графика
plt.xlabel('n')
plt.ylabel('T(n)')
plt.title('Bubble Sort')
plt.legend()
plt.grid(True)

# Отображение графика
plt.show()
