from Clases.Encuestado import Encuestado
from Clases.Pregunta import Pregunta
from Clases.Tema import Tema
from Clases.Encuesta import Encuesta
from AlgoritmoOrd.merge_sort import merge_sort
from controller.controlador import leer_desde_txt

def generar_salida(encuestados, temas, encuesta):
    salida = []
    salida.append("Resultados de la encuesta:\n")

    for idx, tema in enumerate(temas, 1):
        salida.append(f"[{round(tema.promedio_tema(), 2)}] Tema {idx}:")
        for j, pregunta in enumerate(tema.preguntas, 1):
            ids = ', '.join(str(e.id) for e in pregunta.encuestados)
            salida.append(f" [{round(pregunta.promedio_opinion(), 2)}] Pregunta {idx}.{j}: ({ids})")
        salida.append("")

    salida.append("Lista de encuestados:")
    todos = list(encuestados.values())
    ordenados = merge_sort(todos, Encuestado.comparar_por_experticia)
    for e in ordenados:
        salida.append(f" ({e.id}, Nombre:'{e.nombre}', Experticia:{e.experticia}, Opinión:{e.opinion})")
    salida.append("")

    salida.append("Resultados:")
    salida.append(f"  Pregunta con mayor promedio de opinion: [{round(encuesta.pregunta_con_mayor_promedio().promedio_opinion(), 2)}] Pregunta: {encuesta.pregunta_con_mayor_promedio().num_pregunta}")
    salida.append(f"  Pregunta con menor promedio de opinion: [{round(encuesta.pregunta_con_menor_promedio().promedio_opinion(), 2)}] Pregunta: {encuesta.pregunta_con_menor_promedio().num_pregunta}")
    salida.append(f"  Pregunta con mayor promedio de experticia: [{round(max(encuesta.temas, key=lambda t: max(t.preguntas, key=lambda p: p.promedio_experticia()).promedio_experticia()).preguntas[0].promedio_experticia(), 2)}] Pregunta: {max((p for t in encuesta.temas for p in t.preguntas), key=lambda p: p.promedio_experticia()).num_pregunta}")
    salida.append(f"  Pregunta con menor promedio de experticia: [{round(min((p for t in encuesta.temas for p in t.preguntas), key=lambda p: p.promedio_experticia()).promedio_experticia(), 2)}] Pregunta: {min((p for t in encuesta.temas for p in t.preguntas), key=lambda p: p.promedio_experticia()).num_pregunta}")
    salida.append(f"  Pregunta con Mayor mediana de opinion: [{encuesta.mayor_mediana().mediana_opinion()}] Pregunta: {encuesta.mayor_mediana().num_pregunta}")
    salida.append(f"  Pregunta con menor mediana de opinion: [{encuesta.menor_mediana().mediana_opinion()}] Pregunta: {encuesta.menor_mediana().num_pregunta}")
    salida.append(f"  Pregunta con mayor moda de opinion: [{encuesta.pregunta_mayor_moda().moda_opiniones()}] Pregunta: {encuesta.pregunta_mayor_moda().num_pregunta}")
    salida.append(f"  Pregunta con menor moda de opinion: [{encuesta.pregunta_menor_moda().moda_opiniones()}] Pregunta: {encuesta.pregunta_menor_moda().num_pregunta}")
    salida.append(f"  Pregunta con mayor extremismo: [{round(encuesta.pregunta_mayor_extremismo().extremismo_opinion(), 2)}] Pregunta: {encuesta.pregunta_mayor_extremismo().num_pregunta}")
    salida.append(f"  Pregunta con mayor consenso: [{round(encuesta.pregunta_mayor_consenso().consenso_opiniones(), 2)}] Pregunta: {encuesta.pregunta_mayor_consenso().num_pregunta}")

    return '\n'.join(salida)

# --------------------------
# PROGRAMA PRINCIPAL (main)
# --------------------------

archivo_txt = "TestFiles/Test5.txt"  # o donde tengas el archivo
encuestados, temas = leer_desde_txt(archivo_txt)

# Ordenar los temas
temas = merge_sort(temas, Tema.comparar_temas)

# Crear encuesta
encuesta = Encuesta(temas)

# Generar la salida
texto_final = generar_salida(encuestados, temas, encuesta)

# Imprimir por consola
print(texto_final)

# Guardar en archivo de texto
with open("resultados_encuesta.txt", "w", encoding="utf-8") as f:
    f.write(texto_final)
