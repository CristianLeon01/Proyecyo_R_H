from Persona import *
class BusquedaP(Persona):
    def __init__(self, nombre, tipoDocumento, documento, direccion, telefono, estadoCivil, libretaMilitar, correo, apellido, 
                codigoSolicitud, departamento, ciudad, teleTrabajo, sinExperiencia):
        
        super .__init__(nombre, tipoDocumento, documento, direccion, telefono, estadoCivil, libretaMilitar, correo, apellido)

        self.__codigoSolicitud=codigoSolicitud
        self.__departamento=departamento
        self.__ciudad=ciudad
        self.__teleTrabajo=teleTrabajo
        self.__sinExperiencia=sinExperiencia
        self.__busquedaP=[]


    def getCodigoSolicitud(self):
        return self.__codigoSolicitud
    def setCodigoSolicitud(self, codigoSolicitud):
        self.__codigoSolicitud=codigoSolicitud

    def getDepartamento(self):
        return self.__departamento
    def setDepartamento(self, departamento):
        self.__departamento=departamento

    def getCiudad(self):
        return self.__ciudad
    def setCiudad(self, ciudad):
        self.__ciudad=ciudad
    
    def getTeletrabajo(self):
        return self.__teleTrabajo
    def setTeleTrabajo(self, teleTrabajo):
        self.__teleTrabajo=teleTrabajo

    def getSinExperiencia(self):
        return self.__sinExperiencia
    def setsinExperiencia(self, sinExperiencia):
        self.__sinExperiencia=sinExperiencia

    def filtrarDatos (self):
        pass

    def buscarSimilitudes (self):
        pass

    def insertarBusquedaP (self, oferta):
        for i in range (oferta):
            nombreEmpresa = input("Ingrese el nombre de la empresa que desea buscar:")
            if nombreEmpresa == nombreEmpresa:
                print ("Este nombre de empresa si es encontrado dentro de las ofertas")
            else:
                print ("Este nombre de empresa no se encuentra dentro de ninguna oferta")

        for i in range (oferta):
            NITEmpresa = input("Ingrese el NIT de la empresa que desea buscar:")
            if NITEmpresa == NITEmpresa:
                print ("Este NIT si es encontrado dentro de las ofertas")
            else:
                print ("Este NIT no se encuentra dentro de ninguna oferta")

            return nombreEmpresa, NITEmpresa

    
    def agregarBusquedaP (self, busquedaP):
        self.__busquedaP.append(busquedaP)

    def getDatosBusquedaP (self):
        return self.__dict__