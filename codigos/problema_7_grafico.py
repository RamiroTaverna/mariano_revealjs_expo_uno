import numpy as np
import matplotlib.pyplot as plt

# Datos obtenidos del solver
trabajadores = ['A', 'B', 'C']
horas = np.array([10, 50, 60])
costos_por_hora = np.array([20, 18, 15])
costos_totales = horas * costos_por_hora

# Crear figura y ejes
fig, ax1 = plt.subplots(figsize=(8, 5))

# Barra 1: Horas trabajadas
color_horas = 'tab:blue'
ax1.set_xlabel('Trabajadores')
ax1.set_ylabel('Horas trabajadas', color=color_horas)
bar1 = ax1.bar(trabajadores, horas, color=color_horas, label='Horas trabajadas')
ax1.tick_params(axis='y', labelcolor=color_horas)

# Eje secundario para el costo
ax2 = ax1.twinx()
color_costos = 'tab:red'
ax2.set_ylabel('Costo total ($)', color=color_costos)
bar2 = ax2.bar(trabajadores, costos_totales, alpha=0.5, color=color_costos, label='Costo total')
ax2.tick_params(axis='y', labelcolor=color_costos)

# Título y leyenda
plt.title('Horas trabajadas y costo total por trabajador')
fig.tight_layout()

# Mostrar valores arriba de cada barra
for i in range(len(trabajadores)):
    ax1.text(i, horas[i] + 1, f'{horas[i]}h', ha='center', color=color_horas)
    ax2.text(i, costos_totales[i] + 10, f'${costos_totales[i]}', ha='center', color=color_costos)

plt.show()
