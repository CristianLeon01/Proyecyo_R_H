from Empresa import *

class BusquedaE (Empresa):
      def __init__(self,nombre, nit, tipoEmpresa, correo, naturaleza, tipoUsuario, tipoDocumento, documento, contraseña, 
                  cargo, departamento, ciudad, candidatosDepartamento, candidatosMunicipio):
        super().__init__(nombre, nit, tipoEmpresa, correo, naturaleza, tipoUsuario,
                        tipoDocumento, documento, contraseña)
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
     
      def insertarBusquedaE (self, oferta):
        for i in range (oferta):
          mesesExperiencia = input("Ingrese los meses de experiencia de la persona que dese buscar:")
          if mesesExperiencia == mesesExperiencia:
            print ("Estos meses de experiencia si han sido encontrado dentro de las ofertas")
          else:
            print("Estos mese de experiencia no se encuentran dentro de ninguna oferta")

        for i in range (oferta):
          tipoEstudio = input("Ingrese tipo de estudio de la persona que dese buscar:")
          if tipoEstudio == tipoEstudio:
            print ("Este tipo de estudio si es encontrado dentro de las ofertas")
          else:
            print("Este tipo de estudio no se encuentra dentro de ninguna oferta")

          return mesesExperiencia, tipoEstudio
     
      def agregarBusquedaE (self, busquedaE):
        self.__busquedaE.append(busquedaE)

      def getDatosBusquedaE (self):
         return self.__dict__