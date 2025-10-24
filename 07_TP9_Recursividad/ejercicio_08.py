def contar_digito(numero, digito):
    if numero == 0:
        return 0    
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    return contar_digito(numero // 10, digito)