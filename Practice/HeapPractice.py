import numpy as np
import matplotlib.pyplot as plt

ASorted = [0.0, 765.22, 1626.72, 2488.27, 3318.48, 4229.58]
ANearlySorted = [0.0, 758.29, 1596.98, 2516.25, 3421.47, 4363.39]
ARandom = [0.0, 735.38, 1658.0, 2563.35, 3468.56, 4474.37]
ANotSorted = [0.0, 687.74, 1501.97, 2250.21, 3096.0, 3968.18]
n = [0, 100000, 200000, 300000, 400000, 500000]

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
