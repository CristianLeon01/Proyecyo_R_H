from Vacante import Vacante
from Requerimiento import Requerimiento

class Oferta(Vacante, Requerimiento):
    def __init__(self, id, numeroPostulados, fechaPublicacion, fechaCierre, vacantes, postulaciones,
                funcionesContrato, habilidades, competencia, experiencia, jornadaTrabajo, ubicacion, estadoCivil, 
                ocupacion, numVacantes, salario, expMeses, tipoContrato, idOcupacion,
                fechaInscripcion, cargo, candidatosRequeridos, nombreOficio, 
                codDepartamento, codMunicipio, nombreDepartamento, nombreMunicipio):
        
        super().__init__(idOcupacion, fechaInscripcion, cargo, candidatosRequeridos, nombreOficio,
                        codDepartamento, codMunicipio, nombreDepartamento, nombreMunicipio)
        Requerimiento.__init__(self, funcionesContrato, habilidades, competencia, experiencia, jornadaTrabajo,
                            ubicacion, estadoCivil)

        self.__id = id
        self.__numeroPostulados = numeroPostulados
        self.__fechaPublicacion = fechaPublicacion
        self.__fechaCierre = fechaCierre
        self.__vacantes = vacantes
        self.__postulaciones = postulaciones
        self.__oferta = []

    def insertOferta(self):
        
        self.__nombre = input("Ingrese el nombre de la empresa: ")
        self.__nit = input("Ingrese el NIT de la empresa: ")
        self.__tipoEmpresa = input("Ingrese el tipo de empresa: ")
        self.__correo = input("Ingrese el correo de la empresa: ")
        self.__id = input("Ingrese el ID de la oferta: ")
        self.__funcionesContrato = input("Ingrese las funciones del contrato: ")
        self.__habilidades = input("Ingrese las funciones del contrato: ")
        self.__competencia = input("Ingrese las funciones del contrato: ")
        self.__experiencia = input("Ingrese las funciones del contrato: ")
        self.__jornadaTrabajo = input("Ingrese las funciones del contrato: ")
        self.__ubicacion = input("Ingrese las funciones del contrato: ")
        self.__estadoCivil = input("Ingrese las funciones del contrato: ") 
        self.__ocupacion = input("Ingrese las funciones del contrato: ")
        self.__numVacantes = input("Ingrese las funciones del contrato: ")
        self.__salario = input("Ingrese las funciones del contrato: ")
        self.__expMeses = input("Ingrese las funciones del contrato: ")
        self.__tipoContrato = input("Ingrese las funciones del contrato: ")
        self.__idOcupacion = input("Ingrese las funciones del contrato: ")
        self.__cargo = input("Ingrese las funciones del contrato: ")
        self.__candidatosRequeridos = input("Ingrese las funciones del contrato: ")
        self.__nombreOficio = input("Ingrese las funciones del contrato: ")
        self.__fechaInscripcion = input("Ingrese las funciones del contrato: ")
        self.__numeroPostulados = input("Ingrese el número de postulados: ")
        self.__fechaPublicacion = input("Ingrese la fecha de publicación: ")
        self.__fechaCierre = input("Ingrese la fecha de cierre: ")
        self.__vacantes = input("Ingrese el número de vacantes: ")
        self.__postulaciones = input("Ingrese el número de postulaciones: ")
        self.__codDepartamento = input("Ingrese las funciones del contrato: ")
        self.__codMunicipio = input("Ingrese las funciones del contrato: ") 
        self.__nombreDepartamento = input("Ingrese las funciones del contrato: ")
        self.__nombreMunicipio = input("Ingrese las funciones del contrato: ")


        oferta = (self.__nombre, self.__nit, self.__tipoEmpresa, self.__correo, self.__id, self.__funcionesContrato,
                self.__habilidades, self.__competencia, self.__experiencia, self.__jornadaTrabajo, self.__ubicacion, 
                self.__estadoCivil, self.__ocupacion, self.__numVacantes, self.__salario, self.__expMeses, self.__tipoContrato,
                self.__idOcupacion, self.__cargo, self.__candidatosRequeridos, self.__nombreOficio, self.__fechaInscripcion,
                self.__numeroPostulados, self.__fechaPublicacion, self.__fechaCierre, self.__vacantes, self.__postulaciones,
                self.__codDepartamento, self.__codMunicipio, self.__nombreDepartamento, self.__nombreMunicipio)
        
        self.__oferta.append(oferta)

    def getOferta(self):
        print('La oferta es la siguiente:')
        for oferta in self.__oferta:
            return oferta
        
    def filtroOferta():
        pass