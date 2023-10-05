# Texto llamado my_notes.txt
with open("my_notes.txt", "w") as archivo:
    # Escribe al menos tres líneas de notas personales en el archivo
    archivo.write("Nota 1: Universidad Estatal Amazonica.\n")
    archivo.write("Nota 2: Tecnologias de la Informacion.\n")
    archivo.write("Nota 3: Primer Nivel Paralelo: A.\n")

# Lectura del archivo de texto
with open("my_notes.txt", "r") as archivo:
    # Lee el contenido del archivo línea por línea utilizando readline()
    line = archivo.readline()
    while line:
        # Muestra en la consola cada línea leída
        print(line.strip())  # strip() elimina el salto de línea al final de cada línea
        line = archivo.readline()
# Cierre del archivo.
archivo.close()