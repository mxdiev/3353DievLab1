import numpy as np
import matplotlib.pyplot as plt

ASorted = [0.0, 842.23, 1731.97, 2706.79, 3659.54, 4946.11]
ANearlySorted = [0.0, 837.72, 1805.55, 2837.89, 3793.15, 4869.1]
ARandom = [0.0, 1068.38, 2258.77, 3534.57, 4916.9, 6266.25]
ANotSorted = [0.0, 834.77, 1740.08, 2793.85, 3972.95, 4782.57]
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
plt.title('Merge Sort')
plt.legend()
plt.grid(True)
plt.show()
