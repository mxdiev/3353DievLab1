import numpy as np
import matplotlib.pyplot as plt
n = [0, 10000, 20000, 30000, 40000, 50000]
ASorted = [0.0, 2.0, 3.0, 3.87, 6.0, 7.0]
ANearlySorted = [0.0, 49.01, 216.05, 498.18, 966.26, 1648.43]
ARandom = [0.0, 4003.23, 14878.59, 32461.47, 59153.71, 92406.8]
ANotSorted = [0.0, 7607.22, 29166.74, 67023.83, 116085.8, 184699.26]
coefficients1 = np.polyfit(n, ASorted, 2)
coefficients2 = np.polyfit(n, ANearlySorted, 2)
coefficients3 = np.polyfit(n, ARandom, 2)
coefficients4 = np.polyfit(n, ANotSorted, 2)
n_fit = np.linspace(min(n), max(n), 100)
ASorted_fit = np.polyval(coefficients1, n_fit)
ARandom_fit = np.polyval(coefficients3, n_fit)
ANearlySorted_fit = np.polyval(coefficients2, n_fit)
ANotSorted_fit = np.polyval(coefficients4, n_fit)
plt.figure(figsize=(10, 6))

plt.plot(n_fit, ASorted_fit, 'k', label='sorted', linewidth=2)

plt.plot(n_fit, ANearlySorted_fit, 'g', label='nearly sorted', linewidth=2)

plt.plot(n_fit, ARandom_fit, 'b', label='random', linewidth=2)

plt.plot(n_fit, ANotSorted_fit, 'r', label='reverse sorted', linewidth=2)

plt.xlabel('n')
plt.ylabel('T(n)')
plt.title('Insertion Sort')
plt.legend()
plt.grid(True)
plt.show()
