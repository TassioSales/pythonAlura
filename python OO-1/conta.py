class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto....{self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"O titular {self.__titular} tem o Saldo {self.__saldo}")

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor






