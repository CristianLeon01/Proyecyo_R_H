from Postulacion import *
class Oferta(Postulacion):
    def __init__(self, nombre, nit, tipoEmpresa, correo, id, numeroPostulados, fechaPublicacion,
                fechaCierre, vacantes, postulaciones, postulacionAbierta, postulacionCerrada, matriculaAbierta, matriculaCerrada):
        super().__init__(postulacionAbierta, postulacionCerrada, matriculaAbierta, matriculaCerrada)
        self.__nombre = ''
        self.__nit = ''
        self.__tipoEmpresa = ''
        self.__correo = ''
        self.__id = ''
        self.__numeroPostulados = ''
        self.__fechaPublicacion = ''
        self.__fechaCierre = ''
        self.__vacantes = ''
        self.__postulaciones = ''
        self.__oferta = []

    def insertOferta(self):
        
        self.__nombre = input("Ingrese el nombre de la empresa: ")
        self.__nit = input("Ingrese el NIT de la empresa: ")
        self.__tipoEmpresa = input("Ingrese el tipo de empresa: ")
        self.__correo = input("Ingrese el correo de la empresa: ")
        self.__id = input("Ingrese el ID de la oferta: ")
        self.__numeroPostulados = input("Ingrese el número de postulados: ")
        self.__fechaPublicacion = input("Ingrese la fecha de publicación: ")
        self.__fechaCierre = input("Ingrese la fecha de cierre: ")
        self.__vacantes = input("Ingrese el número de vacantes: ")
        self.__postulaciones = input("Ingrese el número de postulaciones: ")
        self.__postulacionAbierta = input("Ingrese si la postulacion esta abierta: ")
        self.__postulacionCerrada = input("Ingrese si la postulacion esta cerrada: ")
        self.__matriculaAbierta = input("Ingrese si la matricula esta abierta: ")
        self.__matriculaCerrada = input("Ingrese si la matricula esta cerrada: ")

        oferta = (self.__nombre, self.__nit, self.__tipoEmpresa, self.__correo, self.__id,
                self.__numeroPostulados, self.__fechaPublicacion, self.__fechaCierre,
                self.__vacantes, self.__postulaciones, self.__postulacionAbierta, 
                self.__postulacionCerrada, self.__matriculaAbierta, self.__matriculaCerrada)
        
        self.__oferta.append(oferta)

    def getOferta(self):
        print('La oferta es la siguiente:')
        for oferta in self.__oferta:
            return oferta
        
    def filtroOferta():
        pass