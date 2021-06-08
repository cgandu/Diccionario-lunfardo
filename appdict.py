import json
from difflib import get_close_matches
data = json.load(open("lunfa.json"))
ejecuta = True
def definicion(termino):
    termino = termino.lower()
    if termino in data:

        return data[termino]

    elif len(get_close_matches(termino, data.keys(), cutoff=0.8)) > 0:
        opcion = input( "Quiso decir %s ? Ingrese 'S' si es correcto o 'N' para buscar nuevamente: " % get_close_matches(termino, data.keys(), cutoff=0.8)[0])
        if opcion.upper() == "S":
            return data[get_close_matches(termino, data.keys(), cutoff=0.8)[0]]
        elif opcion.upper() == "N":
            return "No se encontraron resultados. Pruebe buscando otros terminos %s" % get_close_matches(termino, data.keys(), cutoff=0.4)
        else:
            return "Valor ingresado no es valido"

    elif termino == "/0":
        global ejecuta
        ejecuta = False
        return "Adios"

    else:
        return "Termino no encontrado"


while ejecuta:

    busco = input("Ingrese el termino que busca (o ingrese /0 para salir): ")


    encontrado = definicion(busco)

    if type(encontrado) == list:
        for x in encontrado:
            print(x)
    else:
        print(encontrado)
    