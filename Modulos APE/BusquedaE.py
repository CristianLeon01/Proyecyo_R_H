from Empresa import *
from Ocupacion import *
class BusquedaE (Empresa, Ocupacion):
      def __init__(self,nombre, nit, tipoEmpresa, correo,
                  idOcupacion,fechaInscripcion,cargo,candidatosRequeridos, nombreOficio, 
                  departamento, ciudad, candidatosDepartamento, candidatosMunicipio):
        super().__init__(nombre, nit, tipoEmpresa, correo)
        super().__init__(idOcupacion,fechaInscripcion,cargo,candidatosRequeridos, nombreOficio)
        self.__cargo=cargo
        self.__departamento=departamento
        self.__ciudad=ciudad
        self.__candidatosDepartamento= candidatosDepartamento
        self.__candidatosMunicipio=candidatosMunicipio
        self.__busquedaE=[]

      
      def getCargo(self):
        return self.__cargo
      def setCargo(self, cargo):
        self.__cargo=cargo

      def getDepartamento(self):
        return self.__departamento
      def setDepartamento(self, departamento):
        self.__departamento=departamento

      def getCiudad(self):
        return self.__ciudad
      def setCiudad(self, ciudad):
        self.__ciudad=ciudad

      def getCandidatosDepartamento(self):
        return self.__candidatosDepartamento
      def setCandidatosDeparatamento(self, candidatosDepartamento):
        self.__candidatosDepartamento=candidatosDepartamento

      def getCandidatosMunicipio(self):
        return self.__candidatosMunicipio
      def setCandidatosMunicipio(self, candidatosMunicipio):
        self.__candidatosMunicipio=candidatosMunicipio
   
    
      def filtrarDatos (self):
        pass
     
      def insertarBusquedaE (self):
         cargo = input("Ingrese el cargo que desea buscar:")
         departamento = input("Ingrese el departamento que desea buscar:")
         ciudad = input("Ingrese la ciudad que desea buscar:")
         numCandidatosDepartamento = input("Ingrese el numero de candidatos por departamento que desea buscar:")
         numCandidatosMunicipio = input("Ingrese el numero de candidatos por municipio que desea buscar:")

         return BusquedaE (cargo, departamento, ciudad, numCandidatosDepartamento, numCandidatosMunicipio)
     
      def agregarBusquedaE (self, busquedaE):
        self.__busquedaE.append(busquedaE)

         
      def getBusquedaE (self):
         return self.__dict__
