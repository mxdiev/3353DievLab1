import numpy as np
import matplotlib.pyplot as plt

ASorted = [0.0, 2073.69, 4639.83, 7349.95, 10274.61, 13363.4]
ANearlySorted = [0.0, 2521.13, 5875.14, 9597.67, 14122.44, 19302.7]
ARandom = [0.0, 3032.16, 8276.31, 14503.89, 21264.11, 28928.18]
ANotSorted = [0.0, 2130.65, 4790.41, 7602.18, 11532.22, 13964.48]
n = [0, 200000, 400000, 600000, 800000, 1000000]

coefficients1 = np.polyfit(n, ASorted, 2)
coefficients2 = np.polyfit(n, ANearlySorted, 2)
coefficients3 = np.polyfit(n, ARandom, 2)
coefficients4 = np.polyfit(n, ANotSorted, 2)

# Генерация точек для построения регрессионной кривой
n_fit = np.linspace(min(n), max(n), 100)
ASorted_fit = np.polyval(coefficients1, n_fit)
ARandom_fit = np.polyval(coefficients3, n_fit)
ANearlySorted_fit = np.polyval(coefficients2, n_fit)
ANotSorted_fit = np.polyval(coefficients4, n_fit)

# Построение графика
plt.figure(figsize=(10, 6))

plt.plot(n_fit, ASorted_fit, 'k', label='sorted', linewidth=2)

plt.plot(n_fit, ANearlySorted_fit, 'g', label='nearly sorted', linewidth=2)

plt.plot(n_fit, ARandom_fit, 'b', label='random', linewidth=2)

plt.plot(n_fit, ANotSorted_fit, 'r', label='reverse sorted', linewidth=2)

plt.xlabel('n')
plt.ylabel('T(n)')
plt.title('Heap Sort')
plt.legend()
plt.grid(True)
plt.show()
