from Empresa import *
class Ocupacion:
    def __init__(self,nombre, nit, tipoEmpresa, correo,idOcupacion,fechaInscripcion,cargo,candidatosRequeridos, nombreOficio):
        super().__init__(nombre, nit, tipoEmpresa, correo)
        self.__idOcupacion=idOcupacion
        self.__fechaInscripcion=fechaInscripcion
        self.__cargo=cargo
        self.__candidatosRequeridos=candidatosRequeridos
        self.__nombreOficio=nombreOficio
