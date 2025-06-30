import matplotlib.pyplot as plt
import numpy as np

# Crear valores para x
x = np.linspace(0, 600, 400)

# Restricción 1: x + 1.5y <= 750 => y <= (750 - x) / 1.5
y1 = (750 - x) / 1.5

# Restricción 2: 1.5x + y <= 750 => y <= 750 - 1.5x
y2 = 750 - 1.5 * x

# Crear la figura
plt.figure(figsize=(10, 6))

# Dibujar las áreas factibles
plt.plot(x, y1, label='Oro: x + 1.5y ≤ 750')
plt.plot(x, y2, label='Plata: 1.5x + y ≤ 750')

# Rellenar la zona factible (mínimo entre las dos restricciones)
y = np.minimum(y1, y2)
y = np.maximum(y, 0)  # y no puede ser negativa
plt.fill_between(x, 0, y, where=(y >= 0), color='lightgreen', alpha=0.5, label='Zona factible')

# Punto óptimo conocido (por PuLP)
opt_x = 300
opt_y = 300
plt.plot(opt_x, opt_y, 'ro', label=f'Solución óptima: ({opt_x}, {opt_y})')

# Dibujar una línea de nivel de beneficio (ejemplo: 27000)
# 27000 = 40x + 50y => y = (27000 - 40x) / 50
z = (27000 - 40 * x) / 50
plt.plot(x, z, 'k--', label='Línea de beneficio Z=27000')

# Ajustes del gráfico
plt.xlim(0, 600)
plt.ylim(0, 600)
plt.xlabel('Joyas tipo A (x)')
plt.ylabel('Joyas tipo B (y)')
plt.title('Gráfico del problema de optimización de joyas')
plt.legend()
plt.grid(True)
plt.show()
