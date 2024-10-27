import numpy as np
import matplotlib.pyplot as plt

n = [0, 10000, 20000, 30000, 40000, 50000]
ASorted = [0.0, 3026.94, 12000.5, 27162.19, 48708.12, 78102.72]
ANearlySorted = [0.0, 2997.87, 12408.41, 27438.05, 48991.03, 76384.82]
ARandom = [0.0, 3047.9, 12462.69, 27498.73, 48915.51, 76391.23]
ANotSorted = [0.0, 3146.06, 12867.66, 28487.7, 50868.65, 80039.92]

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
plt.title('Selection Sort')
plt.legend()
plt.grid(True)
plt.show()
