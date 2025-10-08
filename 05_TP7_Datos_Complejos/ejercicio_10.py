import entrada_de_datos as ed
import colecciones as cl

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores. 
capitales_paises = dict()
paises_capitales = {
    "argentina": "buenos aires",
    "brasil": "brasilia",
    "chile": "santiago",
    "uruguay": "montevideo",
    "paraguay": "asuncion",
    "peru": "lima",
    "bolivia": "la paz",
    "colombia": "bogota",
    "venezuela": "caracas",
    "mexico": "ciudad de mexico"
}
ed.dibujar_titulo("Paises con capitales",char='=',cant=3)
cl.mostrar_dicc(paises_capitales)
for k,v in paises_capitales.items():
    capitales_paises[v] = k    
ed.dibujar_titulo("Capitales con paises",char='=',cant=3)
cl.mostrar_dicc(capitales_paises)