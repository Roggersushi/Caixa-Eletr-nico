from historico import Historico

class Conta:

    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()


    def exibir(self):
          print(f'Número da Conta:{self.numero}\n'
                f'Nome do Titular:{self.titular}\n'
                f'Saldo da Conta:{self.saldo}\n'
                f'Limite da Conta:{self.limite}')

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append('depósito de {} '.format(valor))

    def saca(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'O seu novo  saldo é $:{self.saldo}')
            self.historico.transacoes.append('saque de {} '.format(valor))

        else:
            print(f'Vc não tem DINHEIRO!!!!')

    def extrato(self):
        print(f'O saldo da conta de número {self.numero} é R$: {self.saldo}')


    def transfere_para(self,destino,valor):
        if self.saldo >= valor:
           self.saldo -= valor
           destino.saldo += valor
           self.historico.transacoes.append('transferência de {} para conta {}'.format(valor , destino.numero))
           destino.historico.transacoes.append('transferência  {} para conta {} '.format(valor, destino.numero))

        else :
            print(f'Procure um Agiota!!!!{self.saldo}')