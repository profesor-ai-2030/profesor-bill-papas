from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

output = "/home/ubuntu/webdev-static-assets/curriculum-vitae-bill-papas.pdf"
doc = SimpleDocTemplate(output, pagesize=A4, rightMargin=20*mm, leftMargin=20*mm, topMargin=18*mm, bottomMargin=18*mm)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="TitleBP", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=25, leading=29, textColor=colors.HexColor("#203F48"), spaceAfter=4))
styles.add(ParagraphStyle(name="SubtitleBP", parent=styles["Normal"], fontName="Helvetica", fontSize=10, leading=15, textColor=colors.HexColor("#C9794B"), spaceAfter=14))
styles.add(ParagraphStyle(name="HeadingBP", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=colors.HexColor("#203F48"), spaceBefore=14, spaceAfter=6))
styles.add(ParagraphStyle(name="BodyBP", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.5, leading=14, textColor=colors.HexColor("#3D565C"), spaceAfter=5))
styles.add(ParagraphStyle(name="SmallBP", parent=styles["BodyText"], fontName="Helvetica", fontSize=8, leading=11, textColor=colors.HexColor("#68777A")))

story = []
story.append(Paragraph("Profesor Bill Papas", styles["TitleBP"]))
story.append(Paragraph("Tecnología · Ciencia de Datos · Inteligencia Artificial · Robótica", styles["SubtitleBP"]))
story.append(Paragraph("PERFIL PROFESIONAL", styles["HeadingBP"]))
story.append(Paragraph("Profesional especializado en la intersección entre computación, datos, inteligencia artificial, robótica y pensamiento estratégico. Ofrece acompañamiento para convertir preguntas complejas y datos dispersos en decisiones, prototipos y planes de trabajo aplicables.", styles["BodyBP"]))

story.append(Paragraph("ÁREAS DE SERVICIO", styles["HeadingBP"]))
services = [[Paragraph("Diseño Web", styles["BodyBP"]), Paragraph("Análisis de Datos y Estadísticas Empresariales", styles["BodyBP"])], [Paragraph("Inteligencia Artificial", styles["BodyBP"]), Paragraph("Brainstorming e innovación", styles["BodyBP"])], [Paragraph("Google SEO", styles["BodyBP"]), Paragraph("Ciberseguridad y sistemas inteligentes", styles["BodyBP"])]]
t = Table(services, colWidths=[82*mm, 82*mm])
t.setStyle(TableStyle([("GRID", (0,0), (-1,-1), .4, colors.HexColor("#D8D0C2")), ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#F7F3EA")), ("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8), ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7)]))
story.append(t)

story.append(Paragraph("FORMACIÓN ACADÉMICA", styles["HeadingBP"]))
story.append(Paragraph("Fecha de nacimiento indicada: 28/03/1969. La siguiente secuencia representa una cronología estimada a partir del inicio de estudios a los 18 años; no incluye instituciones concretas porque no fueron proporcionadas.", styles["SmallBP"]))
academic = [[Paragraph("1987–1991", styles["BodyBP"]), Paragraph("Bachiller en Ciencias de la Computación", styles["BodyBP"])], [Paragraph("1992–1994", styles["BodyBP"]), Paragraph("Master en Ciencia de Datos", styles["BodyBP"])], [Paragraph("1995–1999", styles["BodyBP"]), Paragraph("Doctorado en Robótica Científica y Análisis Cerebral Robótico", styles["BodyBP"])]]
t2 = Table(academic, colWidths=[34*mm, 130*mm])
t2.setStyle(TableStyle([("LINEBELOW", (0,0), (-1,-1), .4, colors.HexColor("#D8D0C2")), ("TEXTCOLOR", (0,0), (0,-1), colors.HexColor("#C9794B")), ("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 8), ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7)]))
story.append(t2)

story.append(Paragraph("TECNOLOGÍAS Y DISCIPLINAS", styles["HeadingBP"]))
story.append(Paragraph("Big Data · Machine Learning · Ciencia de Datos · Ciberseguridad · Robótica · Python · Análisis Estadístico · Google SEO · Sistemas Inteligentes · Pensamiento Estratégico", styles["BodyBP"]))

story.append(Paragraph("CONTACTO Y REDES", styles["HeadingBP"]))
story.append(Paragraph("GitHub: github.com/profesor-ai-2030<br/>LinkedIn: linkedin.com/in/profesorbillpapas2030/", styles["BodyBP"]))
story.append(Spacer(1, 10))
story.append(Paragraph("© 2026 | Creado por Profesor Bill Papas · © 2026 | Todos los Derechos Reservados", styles["SmallBP"]))

doc.build(story)
print(output)
