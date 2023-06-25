from Empresa import *
from Oferta import *

empresa1 = Empresa('Empresa', 'C.C', 1450368974, 'z78*sd36+AA', 'Mis zapatillas', 123654, 'Asociativa', 'zapatillascol@hotmail.com')
print('Empresa 1:')
print(empresa1.mostrarInfo())

oferta = Oferta.insertOferta()
oferta.agregarOferta(oferta)
print(oferta.getOferta())

empresa2 = Empresa('Empresa', 'C.C', 1578635697, 'dd588SDd221g', 'Sistemas S.A', 578967, 'Asociativa', 'sistemasSs@hotmail.com')
print('Empresa 2:')
print(empresa2.mostrarInfo())
