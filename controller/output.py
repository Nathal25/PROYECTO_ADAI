import sys

class RedireccionarSalida:
    def __init__(self, archivo_salida):
        self.archivo_salida = archivo_salida
        self.salida_original = sys.stdout

    def __enter__(self):
        self.archivo = open(self.archivo_salida, 'w', encoding='utf-8')
        sys.stdout = self.archivo

    def __exit__(self, tipo, valor, traza):
        sys.stdout = self.salida_original
        self.archivo.close()
