from Usuario import *
class Empresa(Usuario):
    def __init__(self,tipoUsuario,nombre,nit,tipoEmpresa,tipoDocumento,documento,correo,naturaleza,contraseña):
        super().__init__(nombre,tipoUsuario,tipoDocumento,documento,contraseña)
        self.__nit=nit
        self.__tipoEmpresa=tipoEmpresa
        self.__correo=correo
        self.__naturaleza=naturaleza
    def crearOferta():
        pass
    
