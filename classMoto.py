class Moto:
    __patente: str
    __marca: str
    __nombreC: str
    __apellidoC: str
    __km: int

    def __init__(self, patente, marca, nombreC, apellidoC, km):
        self.__patente = patente
        self.__marca = marca
        self.__nombreC = nombreC
        self.__apellidoC = apellidoC
        self.__km = km
        
    def __str__(self):
        return f"Patente: {self.__patente}, Marca: {self.__marca}, Nombre Cliente: {self.__nombreC}, Apellido Cliente: {self.__apellidoC}, Kilometraje: {self.__km}"
    def getPatente(self):
        return self.__patente