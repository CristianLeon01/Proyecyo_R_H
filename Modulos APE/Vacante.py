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
