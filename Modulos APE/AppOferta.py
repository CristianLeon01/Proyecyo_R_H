from Empresa import *
from Oferta import *

empresa1 = Empresa('Empresa', 'C.C', 1450368974, 'z78*sd36+AA', 'Mis zapatillas', 123654, 'Asociativa', 'zapatillascol@hotmail.com')
print('Empresa 1:')
print(empresa1.mostrarInfo())

oferta1 = Oferta('nombre', 'nit', 'tipoEmpresa', 'correo', 'id', 'numeroPostulados', 'fechaPublicacion',
                'fechaCierre', 'vacantes', 'postulaciones', 'postulacionAbierta', 'postulacionCerrada', 
                'matriculaAbierta', 'matriculaCerrada')

oferta1.insertOferta()
print(oferta1.getOferta())

empresa2 = Empresa('Empresa', 'C.C', 1578635697, 'dd588SDd221g', 'Sistemas S.A', 578967, 'Asociativa', 'sistemasSs@hotmail.com')
print('Empresa 2:')
print(empresa2.mostrarInfo())

oferta = Oferta.insertOferta()
oferta.agregarOferta(oferta)
print(oferta.getOferta())

persona1 = Persona ('Sergio', 'Ortiz', 'Persona', 'C.C', 'Tecnologo', '27 meses', 'Soy especializado en ciencias del arte', 'Ingles', 23456, 'Calle 22A', 312456789, 'Soltero', 'Si', 'sergio45@gmail.com', '45CSncmj.ty')
print('Persona 1:')
print(persona1.getDatos())

oferta = Oferta.insertOferta()
oferta.agregarOferta(oferta)
print(oferta.getOferta())

persona2 = Persona ('Daniela', 'Perez', 'Persona', 'T.I', 'Tecnico', '24 meses', 'Tengo un tecnico en salud y bienestar', 'Ninguno', 197648, 'Norte 124#', 32157899, 'Soltera', 'No', 'perez@gmail.com', 'Pcer_3456Ad')
print('Persona 2:')
print(persona2.getDatos())

oferta = Oferta.insertOferta()
oferta.agregarOferta(oferta)
print(oferta.getOferta())