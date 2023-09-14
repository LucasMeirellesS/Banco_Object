from random import randint
class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self._caixa = 0
        self.emprestimos = []


    def verificar_caixa(self):
        if self._caixa < 1000000:
            print(f"Caixa abaixo do nível recomendado. Caixa atual: {self._caixa}")
        else:
            print(f"Valor de caixa está ok. Caixa atual:{self._caixa}")


    def emprestar_dinheiro(self, valor, cpf, juros):
        if self._caixa > valor:
            self.emprestimos.append((f"Valor: {valor}", f"CPF:{cpf}", f"Juros: {juros}"))
        else:
            print('Emprestimo não é possível. Dinheiro não disponível em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((f"Nome:{nome}", f"CPF:{cpf}", f"Patrimonio:{patrimonio}"))


class AgenciaVirtual(Agencia):
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self._caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self._caixa -= valor
        self.caixa_paypal += valor
    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self._caixa += valor

class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=f"{randint(1001,9999)}")
        self._caixa = 1000000
class AgenciaPremium(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=f"{randint(1001, 9999)}")
        self._caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print("O cliente não tem o patrimônio mínimo necessário!")


# Teste
if __name__ == "__main__":
    agencia1 = Agencia("9996-5544", "545578", "1584")

    agenciaV = AgenciaVirtual("www.agenciaV.com.br" ,"9995-8877", "5462165")

    agenciaC = AgenciaComum(999554444, 8454321)

    agenciaP = AgenciaPremium(555999888, 99942)
    agenciaV.verificar_caixa()
    agenciaC.verificar_caixa()
    agenciaP.verificar_caixa()

    agenciaV.depositar_paypal(1000)
    print(agenciaV.caixa_paypal)
    """agencia1.caixa = 100000000
    
    agencia1.verificar_caixa()
    
    agencia1.emprestar_dinheiro(1500, "22255599988", 0.02)
    print(agencia1.emprestimos)
    
    agencia1.adicionar_cliente("Lucas", "1145589663958", 100000)
    
    print(agencia1.clientes)"""