import matplotlib.pyplot as plt
import numpy as np

# Datos del Balanced Scorecard
perspectivas = ["Financiera", "Cliente", "Procesos Internos", "Aprendizaje"]
valores = [85, 70, 75, 90]  # Cambia estos valores según tu análisis
max_valor = 100  # Máximo valor posible en cada perspectiva

# Configuración del gráfico
angulos = np.linspace(0, 2 * np.pi, len(perspectivas), endpoint=False).tolist()
valores += valores[:1]  # Cerrar el gráfico
angulos += angulos[:1]

# Crear la figura
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Dibujar el gráfico de radar
ax.fill(angulos, valores, color='skyblue', alpha=0.4)
ax.plot(angulos, valores, color='blue', linewidth=2)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_ylim(0, max_valor)

# Etiquetas y título
ax.set_xticks(angulos[:-1])
ax.set_xticklabels(perspectivas)
ax.set_title("Cuadro de Mando Integral", fontsize=16, pad=20)

# Mostrar el gráfico
plt.tight_layout()
plt.show()
