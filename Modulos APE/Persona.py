from Usuario import *
from Estudio import *
from Postulacion import * 
class Persona(Usuario, Estudio, Postulacion):
    def __init__(self, tipoUsuario, tipoDocumento, documento, contraseña, 
                tipoEstudio, mesesEstudio, descripcion, idiomas,
                postulacionAbierta, postulacionCerrada, matriculaAbierta, matriculaCerrada,
                nombre, apellido, direccion, telefono, estadoCivil, libretaMilitar, correo):
        
        super().__init__(tipoUsuario,tipoDocumento,documento,contraseña)
        super().__init__(tipoEstudio, mesesEstudio, descripcion, idiomas)
        super().__init__(postulacionAbierta, postulacionCerrada, matriculaAbierta, matriculaCerrada)

        self.__nombre=nombre
        self.__apellido=apellido
        self.__direccion=direccion
        self.__telefono=telefono
        self.__estadoCivil=estadoCivil
        self.__libretaMilitar=libretaMilitar
        self.__correo=correo

    def postularse():
        pass

    def getDatos(self):
        return self.__dict__
    