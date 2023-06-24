from Ocupacion import *
from Ubicacion import *
class Vacante(Ocupacion, Ubicacion):
    def __init__(self, idOcupacion,fechaInscripcion,cargo,candidatosRequeridos, nombreOficio, 
                 codDepartamento, codMunicipio, nombreDepartamento, nombreMunicipio,
                 ocupacion, numVacantes, salario, experienciaMeses, tipoContrato):
        super().__init__(idOcupacion,fechaInscripcion,cargo,candidatosRequeridos, nombreOficio)
        super().__init__(codDepartamento, codMunicipio, nombreDepartamento, nombreMunicipio)
        self.__ocupacion=ocupacion
        self.__numVacantes=numVacantes
        self.__salario=salario
        self.__experienciaMeses=experienciaMeses
        self.__tipoContrato=tipoContrato

    def getOcupacion (self):
        return self.__ocupacion
    def setOcupacion(self, ocupacion):
        self.__ocupacion=ocupacion

    def getNumVacantes (self):
        return self.__numVacantes
    def setNumVacantes(self, numVacantes):
        self.__numVacantes=numVacantes

    def getSalario (self):
        return self.__salario
    def setSalario(self, salario):
        self.__salario=salario

    def getExperienciaMeses (self):
        return self.__experienciaMeses
    def setExperienciaMeses(self, experienciaMeses):
        self.__experienciaMeses=experienciaMeses
    
    def getTipoContrato (self):
        return self.__tipoContrato
    def setTipoContrato(self, tipoContrato):
        self.__tipoContrato=tipoContrato