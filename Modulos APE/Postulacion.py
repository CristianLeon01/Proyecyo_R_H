from Persona import *
class Postulacion (Persona):
    def __init__(self, nombre,apellido, tipoUsuario, tipoDocumento, tipoEstudio, mesesEstudio, 
                descripcion, idiomas, documento,direccion,telefono,estadoCivil,libretaMilitar,
                correo, contraseña, postulacionAbierta, postulacionCerrada, matriculaAbierta, 
                matriculaCerrada):
        super().__init__(nombre,apellido, tipoUsuario, tipoDocumento, tipoEstudio,
                        mesesEstudio, descripcion, idiomas, documento,direccion,
                        telefono,estadoCivil,libretaMilitar,correo, contraseña)
        
        self.__postulacionAbierta=postulacionAbierta
        self.__postulacionCerrada=postulacionCerrada
        self.__matriculaAbierta=matriculaAbierta
        self.__matriculaCerrada=matriculaCerrada
