from Usuario import *
class Persona(Usuario):
    def __init__(self, nombre,apellido, tipoUsuario, tipoDocumento,documento,direccion,telefono,estadoCivil,libretaMilitar,correo, contraseña):
        super().__init__(nombre,tipoUsuario,tipoDocumento,documento,contraseña)
        self.__apellido=apellido
        self.__tipoDocumento=tipoDocumento
        self.__documeto=documento
        self.__direccion=direccion
        self.__telefono=telefono
        self.__estadoCivil=estadoCivil
        self.__libretaMilitar=libretaMilitar
        self.__correo=correo
    def postularse():
        pass