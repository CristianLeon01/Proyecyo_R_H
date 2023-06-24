from Postulacion import *
class Oferta(Postulacion):
    def __init__ (self, postulacionAbierta, postulacionCerrada, matriculaAbierta, matriculaCerrada, 
    nombre, nit, tipoEmpresa, correo, id, numeroPostulados, fechaPublicacion, fechaCierre, vacantes, postulaciones):
        #super().__init__(nombre, nit, tipoEmpresa, correo)
        super().__init__(postulacionAbierta, postulacionCerrada, matriculaAbierta, matriculaCerrada)
        self.__id=id
        self.__numeroPostulados=numeroPostulados
        self.__fechaPublicacion=fechaPublicacion
        self.__fechaCierre=fechaCierre
        self.__vacantes=vacantes
        self.__postulaciones=postulaciones
        self.__oferta=[]

    def inserOferta():
        nombre = input("Ingrese el nombre de la empresa: ")
        nit = input("Ingrese el NIT de la empresa: ")
        tipoEmpresa = input("Ingrese el tipo de empresa: ")
        correo = input("Ingrese el correo de la empresa: ")
        id = input("Ingrese el ID de la oferta: ")
        numeroPostulados = input("Ingrese el número de postulados: ")
        fechaPublicacion = input("Ingrese la fecha de publicación: ")
        fechaCierre = input("Ingrese la fecha de cierre: ")
        vacantes = input("Ingrese el número de vacantes: ")
        postulaciones = input("Ingrese el número de postulaciones: ")

        return Oferta (nombre, nit, tipoEmpresa, correo, id, numeroPostulados, fechaPublicacion, fechaCierre, vacantes, postulaciones)
    
    def agregarOferta(self, oferta):
        self.__oferta.append(oferta)
    
    def getOferta(self):
        return self.__dict__
    

    def filtroOferta():
        pass