def merge_sort(lista, comparar):
    if len(lista) <= 1:
        return lista
    mid = len(lista) // 2
    izquierda = merge_sort(lista[:mid], comparar)
    derecha = merge_sort(lista[mid:], comparar)
    return merge(izquierda, derecha, comparar)

def merge(izq, der, comparar):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if comparar(izq[i], der[j]):
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado
