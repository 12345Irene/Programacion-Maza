# Crear el diccionario con información personal ficticia
informacion_personal = {
    "nombre": "Pedro Velez",
    "edad": 35,
    "ciudad": "Quito",
    "profesion": "Licenciado"
}

# Acceder al valor de "ciudad" y modificarlo
informacion_personal["ciudad"] = "Guaranda"

# Agregar la clave-valor de "profesion"
informacion_personal["profesion"] = "Ingeniero"

# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-7890"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario resultante
print(informacion_personal)
