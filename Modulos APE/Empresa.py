from Usuario import Usuario
from Ocupacion import Ocupacion

class Empresa(Usuario, Ocupacion):
    def __init__(self, tipoUsuario, tipoDocumento, documento, contraseña,
                idOcupacion, fechaInscripcion, cargo, candidatosRequeridos, nombreOficio, 
                nombre, nit, tipoEmpresa, correo):
        Usuario.__init__(self, tipoUsuario, tipoDocumento, documento, contraseña)
        Ocupacion.__init__(self, idOcupacion, fechaInscripcion, cargo, candidatosRequeridos, nombreOficio)

        self.__nombre = nombre
        self.__nit = nit
        self.__tipoEmpresa = tipoEmpresa
        self.__correo = correo

    def mostrarInfo(self):
        return self.__nombre, self.__nit, self.__tipoEmpresa, self.__correo
    