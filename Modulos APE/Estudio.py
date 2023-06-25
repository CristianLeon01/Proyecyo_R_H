from Persona import *
class Estudio:
    def __init__(self, nombre, tipoDocumento, documento, direccion, telefono, estadoCivil, libretaMilitar, correo, apellido, 
                 tipoEstudio, mesesEstudio, descripcion, idiomas):
        super().__init__(nombre, tipoDocumento, documento, direccion, telefono, estadoCivil, libretaMilitar, correo, apellido)
        self.__tipoEstudio=tipoEstudio
        self.__mesesEstudio=mesesEstudio
        self.__descripcion=descripcion
        self.__idiomas=idiomas

    def actualizarDatos():
        pass