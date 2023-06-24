from Usuario import *
from Estudio import *
class Persona(Usuario, Estudio):
    def __init__(self, nombre,apellido, tipoUsuario, tipoDocumento, tipoEstudio, mesesEstudio, descripcion, idiomas, documento,direccion,telefono,estadoCivil,libretaMilitar,correo, contraseña):
        super().__init__(tipoUsuario,tipoDocumento,documento,contraseña)
        super().__init__(tipoEstudio, mesesEstudio, descripcion, idiomas)
        self.__nombre=nombre
        self.__apellido=apellido
        self.__direccion=direccion
        self.__telefono=telefono
        self.__estadoCivil=estadoCivil
        self.__libretaMilitar=libretaMilitar
        self.__correo=correo
    def postularse():
        pass