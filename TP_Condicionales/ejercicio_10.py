# Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
# ──────────────────────────────────────────────
# PERÍODOS DEL AÑO SEGÚN HEMISFERIO
# ──────────────────────────────────────────────
#
# HEMISFERIO NORTE:
#   • Invierno  → 21 de diciembre al 20 de marzo
#   • Primavera → 21 de marzo al 20 de junio
#   • Verano    → 21 de junio al 20 de septiembre
#   • Otoño     → 21 de septiembre al 20 de diciembre
#
# HEMISFERIO SUR:
#   • Verano    → 21 de diciembre al 20 de marzo
#   • Otoño     → 21 de marzo al 20 de junio
#   • Invierno  → 21 de junio al 20 de septiembre
#   • Primavera → 21 de septiembre al 20 de diciembre
# ──────────────────────────────────────────────
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
# si el usuario se encuentra en otoño, invierno, primavera o verano.
# Programa que determina la estación del año según hemisferio, mes y día

# Pedir datos
hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
mes = input("Ingrese el mes (ejemplo: marzo): ").lower()
dia = int(input("Ingrese el día: "))
if (mes == "diciembre" and dia >= 21) or mes =="enero" or mes == "febrero" or (mes == "marzo" and dia <= 20):
    estacion = "Invierno" if hemisferio == "norte" else "Verano"
elif (mes == "marzo" and dia >= 21) or mes == "abril" or mes == "mayo" or (mes == "junio" and dia <= 20):
    estacion = "Primavera" if hemisferio == "norte" else "Otoño"
elif (mes == "junio" and dia >= 21) or mes =="julio" or mes == "agosto" or (mes == "septiembre" and dia <= 20):
    estacion = "Verano" if hemisferio == "norte" else "Invierno"
else:
    estacion = "Otoño" if hemisferio == "norte" else "Primavera"
print(f"El {dia} de {mes} en el hemisferio {hemisferio} corresponde a {estacion}.")
