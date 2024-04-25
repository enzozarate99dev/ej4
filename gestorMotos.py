from classMoto import Moto
import csv



class gestorMotos:
    __listaMotos: list

    def __init__(self):
        self.__listaMotos = []

    def cargarMoto(self):
        archivo = open('datosMoto.csv')
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            patente = fila[0]
            marca = fila[1]
            nombreC = fila[2]
            apellidoC = fila[3]
            km = int(fila[4])
            unaMoto = Moto(patente, marca, nombreC, apellidoC, km)
            self.__listaMotos.append(unaMoto)
        archivo.close()

    def mostrar(self):
        for moto in self.__listaMotos:
            print(moto)

    