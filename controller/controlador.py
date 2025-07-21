from Clases.Encuestado import Encuestado
from Clases.Pregunta import Pregunta
from Clases.Tema import Tema

def leer_desde_txt(ruta):
    with open(ruta, encoding='utf-8') as archivo:
        contenido = archivo.read()

    # Dividir el archivo en bloques separados por dos saltos de línea
    bloques = [bloque.strip() for bloque in contenido.split("\n\n") if bloque.strip()]

    # Primer bloque: encuestados
    encuestados = {}
    enc_lines = bloques[0].splitlines()
    for i, linea in enumerate(enc_lines):
        partes = linea.strip().split(",")
        nombre = partes[0].strip()
        experticia = int(partes[1].split(":")[1].strip())
        opinion = int(partes[2].split(":")[1].strip())
        encuestados[i + 1] = Encuestado(i + 1, nombre, experticia, opinion)

    # Los siguientes bloques son temas, cada uno con preguntas
    temas = []
    for t_index, bloque in enumerate(bloques[1:]):
        tema = Tema(f"Tema {t_index + 1}")
        for p_index, linea in enumerate(bloque.splitlines()):
            indices = eval(linea.strip())
            pregunta = Pregunta(f"Pregunta {t_index + 1}.{p_index + 1}")
            for eid in indices:
                pregunta.agregar_encuestado(encuestados[eid])
            tema.agregar_pregunta(pregunta)
        temas.append(tema)

    return encuestados, temas
