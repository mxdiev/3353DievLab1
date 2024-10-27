import numpy as np
import matplotlib.pyplot as plt

ASorted = [0.0, 399.63, 719.23, 1147.94, 1540.96, 2001.57]
ANearlySorted = [0.0, 945.28, 2204.76, 3572.82, 5426.74, 6706.88]
ARandom = [0.0, 1564.37, 3598.67, 5777.21, 9050.53, 11138.38]
ANotSorted = [0.0, 639.87, 1369.25, 2038.76, 3146.33, 3485.63]
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
plt.title('Shell Sort (Shell sequence)')
plt.legend()
plt.grid(True)
plt.show()
