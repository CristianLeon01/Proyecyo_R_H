class Usuario:
    def __init__(self, tipoUsuario, tipoDocumento, documento, contraseña):
        self.__tipoUsuario = tipoUsuario
        self.__tipoDocumento = tipoDocumento
        self.__documento = documento
        self.__contraseña = contraseña

    def mostrarInfo1(self):
        return self.__tipoUsuario, self.__tipoDocumento, self.__documento, self.__contraseña

    def buscarCargo():
        pass