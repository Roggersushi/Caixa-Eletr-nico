
class Conta:
    def __init__(self, numero, cliente, saldo, limite,):
        self.numero = numero
        self.titurlar = cliente
        self.saldo = saldo
        self.limte = limite

    def exibir(self):
          print(f'Número da Conta:{self.numero}\n'
                f'Nome do Titular:{self.titurlar}\n'
                f'Saldo da Conta:{self.saldo}\n'
                f'Limite da Conta:{self.limte}')

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'O seu novo  saldo é $:{self.saldo}')

        else:
            print(f'Vc não tem DINHEIRO!!!!')

    def extrato(self):
        print(f'O saldo da conta de número {self.numero} é R$: {self.saldo}')

    def transfere(self,destino,valor):
        if self.saldo >= valor:
           self.saldo -= valor
           destino.saldo += valor

        else :
            print(f'Procure um Agiota!!!!{self.saldo}')
