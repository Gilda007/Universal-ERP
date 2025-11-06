# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter, A4
# my_path = 'C:\\Users\\Gilda ENADA\Downloads\\test.pdf'
# c= canvas.Canvas(my_path, pagesize=letter)
# c.translate(inch, inch)
# c.setStrokeColorRGB(1,0,0)
# c.setLineWidth(10)
# c.line(0,8*inch,7*inch,8*inch)
# c.drawImage('C:\\Users\\Gilda ENADA\\OneDrive\\Documents\Projet MINDCAF\\Gesion de caisse\\Utilisateur\images\\OIP.jpg', -0.8*inch,6.3*inch)

# c.rotate(45)
# c.setFillColorCMYK(0,0,0,0.08)
# c.setFont('Helvetica', 50)
# c.drawString(2*inch,1*inch, 'SECRETARIAT')
# c.rotate(-45)
# c.showPage()
# c.save()

# Initialisation de la variable en dehors du bloc try-except
# ma_variable = None
# try:
#     # Tentative d'opération qui peut générer une exception
#     ma_variable = 10 / 2
# except ZeroDivisionError as e:
#     # Traitement de l'exception
#     print("Une erreur s'est produite :", e)

# # Accès à la variable à l'extérieur du bloc try-except
# print("La valeur de ma_variable est :", ma_variable)
#
#print(instance_classe.try_exemple())

# Appel de la fonction fonction_interne en dehors du bloc try (impossible)
# print(fonction_interne())  # Cela lèvera une erreur NameError car fonction_interne n'est pas définie ici

ok=29*12
print(ok)