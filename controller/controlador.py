import csv
from Clases.Encuestado import Encuestado
def leer_encuestados_desde_csv(ruta):
    encuestados = {}
    with open(ruta, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            eid = int(fila["id"])
            nombre = fila["nombre"]
            experticia = int(fila["experticia"])
            opinion = int(fila["opinion"])
            encuestados[eid] = Encuestado(eid, nombre, experticia, opinion)
    return encuestados

