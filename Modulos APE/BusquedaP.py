#BusquedaP.py

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
        self.__busquedaP=[]

    def getCargo(self):
        return self.__departamento
    def setDepartamento(self, departamento):
        self.__departamento=departamento

    def filtrarDatos (self):
        pass

    def buscarSimilitudes (self):
        pass

    def insertarBusquedaP (self):
        codigoSolicitud = input("Ingrese el codigo de solicitud para realizar la bsuqueda:")
        departamento = input("Ingrese el departamento donde desea realizar la busqueda:")
        ciudad = input("Ingrese la ciudad donde desea realizar la busqueda:")
        teletrabajo = input("Ingrese si desea buscar por teletrabajo:")
        sinExperiencia = input("Ingrese si desea buscar por sin experincia:")
        economiaNaranja = input("Ingrese si desea buscar por economia naranaja:")

        return codigoSolicitud, departamento, ciudad, teletrabajo, sinExperiencia, economiaNaranja
    
    def agregarBusquedaP (self, busquedaP):
        self.__busquedaP.append(busquedaP)
    