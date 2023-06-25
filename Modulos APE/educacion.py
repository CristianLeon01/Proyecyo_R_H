from datos_basicos import *
class educacion:
    def __init__(self,primaria,secundaria,superior):
        self.__primaria=primaria
        self.__secundaria=secundaria
        self.__superior=superior
    def get_primaria(self):
        return self.__primaria
    def get_secundaria(self):
        return self.__secundaria
    def get_superior(self):
        return self.__superior
a1=educacion('si','no','no')
print(a1.get_primaria())
print(a1.get_secundaria())
print(a1.get_superior())