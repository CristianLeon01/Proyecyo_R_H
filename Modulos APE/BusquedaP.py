#BusquedaP.py
from Oferta import *
from Persona import *
class BusquedaP (Oferta, Persona):
    def __init__(self, id, numeroPostulados, fechaPublicacion, fechaCierre, vacantes, postulaciones,
                 nombre, tipoDocumento, documento, direccion, telefono, estadoCivil, libretaMilitar, correo, apellido, 
                cargo, codigoSolicitud, departamento, ciudad, teleTrabajo, sinExperiencia, economiaNaranja):
        super().__init__(id, numeroPostulados, fechaPublicacion, fechaCierre, vacantes, postulaciones)
        super .__init__(nombre, tipoDocumento, documento, direccion, telefono, estadoCivil, libretaMilitar, correo, apellido)
        self.__cargo=cargo
        self.__codigoSolicitud=codigoSolicitud
        self.__departamento=departamento
        self.__ciudad=ciudad
        self.__teleTrabajo=teleTrabajo
        self.__sinExperiencia=sinExperiencia
        self.__economiaNaranja=economiaNaranja
        self.__busquedaP=[]

    def filtrarDatos (self):
        pass

    def buscarSimilitudes (self):
        pass

    def insertarBusquedaP (self, oferta):
        for i in self.__oferta:
            nombreEmpresa = input("Ingrese el nombre de la empresa que desea buscar:")
            if nombreEmpresa == nombreEmpresa:
                print ("Este nombre de empresa si es encontrado dentro de las ofertas")
            else:
                print ("Este nombre de empresa no se encuentra dentro de ninguna oferta")

        for i in self.__oferta:
            NITEmpresa = input("Ingrese el NIT de la empresa que desea buscar:")
            if NITEmpresa == NITEmpresa:
                print ("Este NIT si es encontrado dentro de las ofertas")
            else:
                print ("Este NIT no se encuentra dentro de ninguna oferta")

            return oferta

    
    def agregarBusquedaP(self,busquedaP):
        self.__busquedaP.append(busquedaP)

    def getDatosBusquedaP (self):
        return self.__cargo, self.__codigoSolicitud, self.__departamento, self.__ciudad, self.__teleTrabajo, self.__sinExperiencia, self.__economiaNaranja, self.__busquedaP