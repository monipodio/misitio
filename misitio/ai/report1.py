from reportlab.lib.pagesizes import A4
from reportlab.platypus import *
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas

c = canvas.Canvas("hola-mundo.pdf")
c.drawString(50, 50, "¡Hola, mundo!")
c.save()

