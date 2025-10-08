import entrada_de_datos as ed
import colecciones as cl
# 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra.

# frase = 'El sol brilla sobre el mar, el sol calienta la arena, y el mar canta con olas suaves y frescas.'
frase = ed.pedir_cadena('Ingrese una frase: ',largo=150)
palabras = frase.replace(',','').replace('.',' ').strip().lower().split()
palabras_unicas = set(palabras)
palabras_cantidad = dict()
for palabra in palabras_unicas:
    palabras_cantidad[palabra] = palabras.count(palabra)
print(f'FRASE INGRESADA: \'{frase}\'')
ed.dibujar_titulo('palabras unicas',char='=',cant=2)
cl.mostrar_lista(palabras_unicas)
ed.dibujar_titulo('Cantidad de repeticiones',char='=',cant=2)
cl.mostrar_dicc(palabras_cantidad)