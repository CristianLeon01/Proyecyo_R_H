from Postulacion import Postulacion

class Oferta(Postulacion):
    def __init__(self, postulacionAbierta, postulacionCerrada, matriculaAbierta, matriculaCerrada,
                nombre, nit, tipoEmpresa, correo, id, numeroPostulados, fechaPublicacion, fechaCierre, vacantes, postulaciones):
        super().__init__(postulacionAbierta, postulacionCerrada, matriculaAbierta, matriculaCerrada)
        self.__id = id
        self.__numeroPostulados = numeroPostulados
        self.__fechaPublicacion = fechaPublicacion
        self.__fechaCierre = fechaCierre
        self.__vacantes = vacantes
        self.__postulaciones = postulaciones
        self.__oferta = []

    @classmethod
    def insertOferta(cls):
        nombre = input("Ingrese el nombre de la empresa: ")
        nit = input("Ingrese el NIT de la empresa: ")
        tipoEmpresa = input("Ingrese el tipo de empresa: ")
        correo = input("Ingrese el correo de la empresa: ")
        id = input("Ingrese el ID de la oferta: ")
        numeroPostulados = input("Ingrese el número de postulados: ")
        fechaPublicacion = input("Ingrese la fecha de publicación: ")
        fechaCierre = input("Ingrese la fecha de cierre: ")
        vacantes = input("Ingrese el número de vacantes: ")
        postulaciones = input("Ingrese el número de postulaciones: ")

        return cls(True, False True, False, nombre, nit, tipoEmpresa, correo, id, numeroPostulados,
                fechaPublicacion, fechaCierre, vacantes, postulaciones)

    def agregarOferta(self, oferta):
        self.__oferta.append(oferta)

    def __str__(self):
        return f"Oferta:\n\nID: {self.__id}\nNúmero de Postulados: {self.__numeroPostulados}\n" \
            f"Fecha de Publicación: {self.__fechaPublicacion}\nFecha de Cierre: {self.__fechaCierre}\n" \
            f"Vacantes: {self.__vacantes}\nPostulaciones: {self.__postulaciones}"


    def filtroOferta():
        pass