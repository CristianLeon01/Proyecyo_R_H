from BusquedaE import *
from BusquedaP import *

busquedaE = BusquedaE.insertarBusquedaE(())
busquedaE.agregarBusquedaE(busquedaE)

print(busquedaE.getBusquedaE())


busquedaP = BusquedaP.insertarBusquedaP()
busquedaP.agregarBusquedaP(busquedaP)

print(busquedaP.getBusquedaP())