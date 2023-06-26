from Usuario import *
class Empresa(Usuario):
    def __init__(self, tipoUsuario, tipoDocumento, documento, contraseña, nombre, nit, tipoEmpresa, correo):
        super().__init__(tipoUsuario, tipoDocumento, documento, contraseña)
        self.__nombre=nombre
        self.__nit=nit
        self.__tipoEmpresa=tipoEmpresa
        self.__correo=correo

    def mostrarInfo (self):
        return self.__nombre, self.__nit, self.__tipoEmpresa, self.__correo
    