import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from PIL import Image

# Crear gráficos de ejemplo
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 16, 9, 4, 1]

# Gráfico 1
plt.figure()
plt.plot(x, y1, marker='o', label="Cuadrados")
plt.title("Gráfico 1: Cuadrados de números")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
buffer1 = BytesIO()
plt.savefig(buffer1, format='png')
buffer1.seek(0)
plt.close()

# Gráfico 2
plt.figure()
plt.plot(x, y2, marker='s', color="red", label="Inverso")
plt.title("Gráfico 2: Inverso de cuadrados")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
buffer2 = BytesIO()
plt.savefig(buffer2, format='png')
buffer2.seek(0)
plt.close()

# Crear un archivo PDF con ReportLab
pdf_file = r"C:\ruta"
c = canvas.Canvas(pdf_file, pagesize=letter)
width, height = letter

# Encabezado con diseño
c.setFont("Helvetica-Bold", 20)
c.drawString(30, height - 50, "Reporte Detallado de Gráficos")
c.setFont("Helvetica", 12)
c.drawString(30, height - 70, "Generado automáticamente con Python y Matplotlib")
c.drawString(30, height - 85, "Este reporte incluye un análisis visual y descriptivo.")

# Primera sección: Gráfico 1 y texto a su lado
c.setFont("Helvetica-Bold", 16)
c.drawString(30, height - 120, "1. Cuadrados de números")

c.setFont("Helvetica", 10)
c.drawString(30, height - 140, "Descripción:")
c.drawString(30, height - 155, "- Este gráfico muestra cómo los números se elevan al cuadrado.")
c.drawString(30, height - 170, "- Es útil para observar el crecimiento cuadrático.")
c.drawString(30, height - 185, "- Estadísticas:")
c.setFont("Helvetica-Bold", 12)
c.drawString(50, height - 200, f"  Máximo: {max(y1)}")
c.drawString(50, height - 215, f"  Mínimo: {min(y1)}")
c.drawString(50, height - 230, f"  Media: {sum(y1)/len(y1):.2f}")

# Insertar gráfico 1 al lado derecho del texto
image1 = Image.open(buffer1)
c.drawInlineImage(image1, 300, height - 400, width=250, height=200)

# Segunda sección: Gráfico 2 y texto a su lado
c.setFont("Helvetica-Bold", 16)
c.drawString(30, height - 450, "2. Inverso de cuadrados")

c.setFont("Helvetica", 10)
c.drawString(30, height - 470, "Descripción:")
c.drawString(30, height - 485, "- Este gráfico representa el inverso de los cuadrados.")
c.drawString(30, height - 500, "- Se utiliza para analizar tendencias decrecientes.")
c.drawString(30, height - 515, "- Estadísticas:")
c.setFont("Helvetica-Bold", 12)
c.drawString(50, height - 530, f"  Máximo: {max(y2)}")
c.drawString(50, height - 545, f"  Mínimo: {min(y2)}")
c.drawString(50, height - 560, f"  Media: {sum(y2)/len(y2):.2f}")

# Insertar gráfico 2 al lado derecho del texto
image2 = Image.open(buffer2)
c.drawInlineImage(image2, 300, height - 730, width=250, height=200)

# Guardar el PDF
c.save()

print(f"PDF generado exitosamente en {pdf_file}.")
