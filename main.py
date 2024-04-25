from gestorMotos import gestorMotos
from gestorPedido import gestorPedidos




if __name__ == "__main__":
    gm = gestorMotos()
    gp = gestorPedidos()
    print("Motos")
    gm.cargarMoto()
    gm.mostrar()
    print("Pedidos del archivo")
    gp.cargarPedido()
    gp.mostrar()
    while True:
        print("1. Crear nuevo pedido")
        print("2. Modificar tiempo real de entrega")
        print("3. Mostrar pedidos actualizados")
        print("\n4. Calcular Total de todas las sucursales")
        print("\n0. Salir")
        op= int(input("Ingrese una opcion: "))
        if op == 1:
            pat = input("Ingrese la patente: ")
            gp.crearPedido(pat)
        elif op == 2:
            pat = input("Ingrese la patente: ")
            id = int(input("Ingrese el identificador del pedido: "))
            tiempoR = int(input("Ingrese el tiempo real de entrega del pedido: "))
            gp.modifPed(pat, id, tiempoR)
        elif op == 3:
            print("Pedidos actualizados")
            gp.mostrar()
            
       # elif op == 4: 
            #print(f"El total recaudado de la semana es: {venta.calcularTotal()}")
            
        elif op == 0:
            print("SALIENDO...")
            break
    
    
