from classPedido import Pedido
import csv


class gestorPedidos:
    __listaPedidos: list

    def __init__(self):
        self.__listaPedidos = []

    def cargarPedido(self):
        archivo = open('datosPedido.csv')
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            patente = fila[0]
            id = int(fila[1])
            comida = fila[2]
            tiempoE = int(fila[3])
            importe = int(fila[4])
            unPedido = Pedido(patente, id, comida, tiempoE,importe)
            self.__listaPedidos.append(unPedido)
        archivo.close()

    def mostrar(self):
        for ped in self.__listaPedidos:
            print(ped)
    
    def crearPedido(self, xpat):
        i=0
        while i<len(self.__listaPedidos) and xpat != self.__listaPedidos[i].getPatente():
            i=i+1
        try:
            if xpat == self.__listaPedidos[i].getPatente():
                pat = xpat
                id = int(input("Ingrese el id del pedido: "))
                comida = input("Ingrese las comidas: ")
                tiempoE = int(input("Ingrese el tiempo estimado en minutos: "))
                imp = int(input("Ingrese el importe: "))
                newPed = Pedido(pat, id, comida, tiempoE, imp)
                self.__listaPedidos.append(newPed)
            
        except IndexError:
            print("La patente no se encuentra")

    def modifPed(self, xpat, xid, xtr):
        i=0
        while i<len(self.__listaPedidos) and (xpat != self.__listaPedidos[i].getPatente() or xid != self.__listaPedidos[i].getId()):
            i=i+1
            try:
                if xpat == self.__listaPedidos[i].getPatente() and xid != self.__listaPedidos[i].getId():
                    self.__listaPedidos[i].setTiempoR(xpat, xid, xtr)
            except IndexError:
                print("No coinciden patente y/o codigo del pedido")




