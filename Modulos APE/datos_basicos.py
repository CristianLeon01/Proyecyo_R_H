from actualizacion_datos import *

class datos_basicos:

    datos_identificacion=[]
    identidad=[]
    datos_nacimiento=[]
    estado_civil=[]
    domicilio=[]
    sisben=[]
    datos_contacto=[]
    situacion_ocupacional=[]
    def __init__(self):
        self.__datos_identificacion=[]
        self.__identidad=[]
        self.__datos_nacimiento=[]
        self.__estado_civil=[]
        self.__domicilio=[]
        self.__sisben=[]
        self.__datos_contacto=[]
        self.__situacion_ocupacional=[]

    def get_datos_identificacion(self):
        return self.__datos_identificacion
    def set_datos_identificacion(self,datos_identificacion):
        self.__datos_identificacion.append(datos_identificacion)
        for a in self.__datos_identificacion:
            if a not in datos_basicos.datos_identificacion:
                datos_basicos.datos_identificacion.append(a)

    def get_identidad(self):
        return self.__identidad
    def set_identidad(self,identidad):
        self.__identidad.append(identidad)
        for a in self.__identidad:
            if a not in datos_basicos.identidad:
                datos_basicos.identidad.append(a)

    def get_datos_nacimiento(self):
        return self.__datos_nacimiento
    def set_datos_nacimiento(self,datos_nacimiento):
        self.__datos_nacimiento.append(datos_nacimiento)
        for a in self.__datos_nacimiento:
            if a not in datos_basicos.datos_nacimiento:
                datos_basicos.datos_nacimiento.append(a)

    def get_estado_civil(self):
        return self.__estado_civil
    def set_estado_civil(self,estado_civil):
        self.__estado_civil.append(estado_civil)
        for a in self.__estado_civil:
            if a not in datos_basicos.estado_civil:
                datos_basicos.estado_civil.append(a)

    def get_domicilio(self):
        return self.__domicilio
    def set_domicilio(self,domicilio):
        self.__domicilio.append(domicilio)
        for a in self.__domicilio:
            if a not in datos_basicos.domicilio:
                datos_basicos.domicilio.append(a)

    def get_sisben(self):
        return self.__sisben
    def set_sisben(self,sisben):
        self.__sisben.append(sisben)
        for a in self.__sisben:
            if a not in datos_basicos.sisben:
                datos_basicos.sisben.append(a)

    def get_datos_contacto(self):
        return self.__datos_contacto
    def set_datos_contacto(self,datos_contacto):
        self.__datos_contacto.append(datos_contacto)
        for a in self.__datos_contacto:
            if a not in datos_basicos.datos_contacto:
                datos_basicos.datos_contacto.append(a)

    def get_situacion_ocupacional(self):
        return self.__situacion_ocupacional
    def set_situacion_ocupacional(self,situacion_ocupacional):
        self.__situacion_ocupacional.append(situacion_ocupacional)
        for a in self.__situacion_ocupacional:
            if a not in datos_basicos.situacion_ocupacional:
                datos_basicos.situacion_ocupacional.append(a)