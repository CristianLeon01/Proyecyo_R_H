from Persona import *
class Postulacion (Persona):
    def __init__(self, nombre, tipoDocumento, documento, direccion, telefono, estadoCivil, libretaMilitar, correo, apellido,
     postulacionAbierta, postulacionCerrada, matriculaAbierta, matriculaCerrada):
        super().__init__(nombre, tipoDocumento, documento, direccion, telefono, estadoCivil, libretaMilitar, correo, apellido)
        self.__postulacionAbierta=postulacionAbierta
        self.__postulacionCerrada=postulacionCerrada
        self.__matriculaAbierta=matriculaAbierta
        self.__matriculaCerrada=matriculaCerrada
