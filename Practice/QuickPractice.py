import numpy as np
import matplotlib.pyplot as plt

ASorted = [0.0, 373.63, 802.22, 1168.87, 1691.55, 1996.37]
ANearlySorted = [0.0, 383.65, 805.81, 1237.4, 1711.03, 2196.73]
ARandom = [0.0, 526.67, 1166.89, 2041.16, 2782.93, 3618.52]
ANotSorted = [0.0, 377.09, 793.73, 1196.34, 1667.16, 1971.63]
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
plt.title(Quick Sort')
plt.legend()
plt.grid(True)
plt.show()
