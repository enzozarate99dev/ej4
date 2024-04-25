class Pedido:
    __patente: str
    __id: str
    __comida: str
    __tiempoE: int
    __tiempoReal: int
    __importe: int

    def __init__(self, patente, id, comida, tiempoE, imp):
        self.__patente = patente
        self.__id = id
        self.__comida = comida
        self.__tiempoE = tiempoE
        self.__importe = imp
        self.__tiempoReal = 0
    
    def __str__(self):
        return f"Patente: {self.__patente}, Id: {self.__id}, Comidas: {self.__comida}, T estimado: {self.__tiempoE},Importe: {self.__importe} ,t real: {self.__tiempoReal}"
        
    def getPatente(self):
        return self.__patente
    
    def getId(self):
        return self.__id
    
    def setTiempoR(self, xtr):
        self.__tiempoReal = xtr

   