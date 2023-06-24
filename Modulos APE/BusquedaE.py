from Empresa import *
from Ocupacion import *
class BusquedaE (Empresa, Ocupacion):
     def __init__(self,nombre, nit, tipoEmpresa, correo, 
     idOcupacion,fechaInscripcion,cargo,candidatosRequeridos, nombreOficio,
     cargo, departamento, ciudad, candidatosDepartamento, candidatosMunicipio):
        super().__init__(nombre, nit, tipoEmpresa, correo)
        super().__init__(idOcupacion,fechaInscripcion,cargo,candidatosRequeridos, nombreOficio)
        self.__cargo=cargo
        self.__departamento=departamento
        self.__ciudad=ciudad
        self.__candidatosDepartamento= candidatosDepartamento
        self.__candidatosMunicipio=candidatosMunicipio
    
     def filtrarDatos (self):
        pass
