from datetime import datetime
from random import randint

class ContaCorrente:

    @staticmethod
    def _get_data_hora():
        horario_BR = datetime.now()
        return horario_BR.strftime("%d/%m/%Y %H:%M:%S")

    def __init__(self, nome, cpf, agencia, num_conta, saldo = 0, limite = 0):
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        self.__limite = limite
        self.__agencia = agencia
        self.__num_conta = num_conta
        self.__transacoes = []
        self.cartoes = []


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf:str):
        self.__cpf = cpf

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo:float):
        self.__saldo = saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite:float):
        self.__limite = limite

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia:str):
        self.__agencia = agencia

    @property
    def num_conta(self):
        return self.__num_conta

    @num_conta.setter
    def num_conta(self, num_conta:str):
        self.__num_conta = num_conta

    '''def registra_card(self, cartao):
        self.__cartoes.append(cartao)'''

    def consultar_historico_transacoes(self):
        print('Histórico de Transações:')
        print('Valor, Saldo, Data e Hora')
        for transacao in self.__transacoes:
            print(transacao)

    def consultar_cartoes(self):
        print('Cartões:')
        for cartao in self.cartoes:
            print(cartao.__dict__)


    def _registra_transacao(self, transacao):
        self.__transacoes.append(transacao)

    def _add_transacao(self, valor: float, tipo: int, conta = None):
        transacao = ()

        if tipo == 1:
            transacao = (
            f"Saque de R${valor:.2f}", f"Total anterior:{self.saldo + valor}", f"Total atual: {self.saldo}",
            f"Data e Hora: {ContaCorrente._get_data_hora()}")


        elif tipo == 2:
            transacao = (
            f"Deposito de R${valor:.2f}", f"Total anterior:{self.saldo - valor}", f"Total atual: {self.saldo}",
            f"Data e Hora: {ContaCorrente._get_data_hora()}")


        elif tipo == 3 and conta is not None:
            transacao = (
            f"Transferência de R${valor:.2f} para {conta.nome}", f"Total anterior: {self.saldo + valor}",
            f"Total atual: {self.saldo}", f"Data e Hora: {ContaCorrente._get_data_hora()}")

        elif tipo == 4 and conta is not None:
            transacao = (
            f"Recebeu o valor de R${valor:.2f} de {conta.nome}", f"Total anterior: {self.saldo - valor}",
            f"Total atual: {self.saldo}", f"Data e Hora: {ContaCorrente._get_data_hora()}")

        self._registra_transacao(transacao=transacao)

    def consulta_saldo(self, saldo):
        return f"Seu saldo é de R$ {self.saldo:.2f}"

    def sacar(self, valor:float, transferencia = False, conta = None):
        if self.saldo - valor < self.limite:
            print(f"Valor acima do limite da conta!")

        else:
            self.saldo -= valor
            if transferencia is True:
                self._add_transacao(valor, tipo=3, conta= conta)
            else:
                self._add_transacao(valor, tipo=1)

    def depositar(self, valor:float, recebimento = False, conta=None):
        self.saldo += valor
        if recebimento is True:
            self._add_transacao(valor, tipo=4, conta = conta)
        else:
            self._add_transacao(valor, tipo=2)

    def transferir(self, valor, conta):
        self.sacar(valor=valor, transferencia= True, conta=conta)
        conta.depositar(valor=valor, recebimento= True, conta=self)


class CartaoCredito:
    @staticmethod
    def _data_hora():
        horario_BR = datetime.now()
        return horario_BR

    def __init__(self, numero, conta_corrente):
        self.numero = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)} {randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)} " \
                      f"{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)} {randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}"
        self.titular = conta_corrente.nome
        self.limite = 1000
        self.validade = f"{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}"
        self.cod_seguranca = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}"
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)



    

conta1 = ContaCorrente("Zé", "044-744-895.65", "5555-111", "55559999")
cartao1 = CartaoCredito("Lucas", conta1)

print(cartao1.conta_corrente.num_conta)
conta1.consultar_cartoes()