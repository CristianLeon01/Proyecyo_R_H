from Empresa import *
from Oferta import *

empresa1 = Empresa('Empresa', 'C.C', 1450368974, 'z78*sd36+AA', 'Mis zapatillas', 123654, 'Asociativa', 'zapatillascol@hotmail.com')
print('Empresa 1:')
print(empresa1.mostrarInfo())
print(empresa1.mostrarInfo1())
print()

oferta = Oferta.insertOferta()
oferta.agregarOferta(oferta)

print(oferta.getOferta())