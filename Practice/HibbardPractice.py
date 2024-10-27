import numpy as np
import matplotlib.pyplot as plt

ASorted = [0.0, 341.71, 709.7, 1110.3, 1516.02, 1937.57]
ANearlySorted = [0.0, 846.99, 2119.36, 3864.82, 4918.49, 6738.48]
ARandom = [0.0, 1281.89, 3496.06, 5915.43, 7943.43, 10371.71]
ANotSorted = [0.0, 537.77, 1087.4, 1874.54, 2341.21, 2958.34]
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
