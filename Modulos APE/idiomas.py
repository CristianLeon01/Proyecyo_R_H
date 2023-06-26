from Datos_basicos import *
class idiomas:
    def __init__(self,idioma,dialecto):
        self.__idioma=idioma
        self.__dialecto=dialecto
    def get_idioma(self):
        return self.__idioma
    def get_dialecto(self):
        return self.__dialecto
a1=idiomas('ingles', 'guaibo')
print(a1.get_idioma())
print(a1.get_dialecto())