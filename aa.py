import matplotlib.pyplot as plt
import numpy as np

# Függvény definiálása
def k(x):
    return 0.4 * (x - 2)**2

# x értékek generálása
x_values = np.linspace(-1, 5, 400)
# függvény értékek kiszámítása
y_values_k = k(x_values)

# Ábrázolás
plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values_k, label='k(x) = 0.4(x-2)^2')
plt.scatter([2], [0], color='red', marker='o')  # Csúcs pirossal jelölve
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('k(x) = 0.4(x-2)^2 függvény')
plt.xlabel('x')
plt.ylabel('k(x)')
plt.show()
