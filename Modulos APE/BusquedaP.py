from Persona import *
class BusquedaP (Persona):
    def __init__(self, nombre, tipoDocumento, documento, direccion, telefono, estadoCivil, libretaMilitar, correo, apellido, 
    cargo, codigoSolicitud, departamento, ciudad, teleTrabajo, sinExperiencia, economiaNaranja):
        super .__init__(nombre, tipoDocumento, documento, direccion, telefono, estadoCivil, libretaMilitar, correo, apellido)
    self.__cargo=cargo
    self.__codigoSolicitud=codigoSolicitud
    self.__departamento=departamento
    self.__ciudad=ciudad
    self.__teleTrabajo=teleTrabajo
    self.__sinExperiencia=sinExperiencia
    self.__economiaNaranja=economiaNaranja

    def filtrarDatos (self):
        pass

    def buscarSimilitudes (self):
        pass
