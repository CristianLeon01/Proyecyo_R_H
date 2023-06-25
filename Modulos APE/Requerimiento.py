from Oferta import *
class Requerimiento (Oferta):
    def __init__(self, nombre, nit, tipoEmpresa, correo, id, numeroPostulados, fechaPublicacion, fechaCierre, vacantes, postulaciones, funcionesContrato, habilidades, competencia, experiencia, jornadaTrabajo, ubicacion, estadoCivil):
        super().__init__(nombre, nit, tipoEmpresa, correo, id, numeroPostulados, fechaPublicacion, fechaCierre, vacantes, postulaciones)
        self.__funcionesContrato=funcionesContrato
        self.__habilidades=habilidades
        self.__competencia=competencia
        self.__experiencia=experiencia
        self.__jornadaTrabajo=jornadaTrabajo
        self.__ubicacion=ubicacion
        self.__estadoCivil=estadoCivil

