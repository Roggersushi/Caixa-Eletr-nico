from conta import*
from cliente import*

if __name__ == '__main__':
    cliente = Cliente('Fabrici', 'Dias', '125-078-304-01')
    conta1 = Conta('123-5', cliente, 120.00, 500.00)
    cliente2 = Cliente('Brenno' , 'Viana' ,'111-111-000-00')
    conta2 = Conta('234-5', cliente2, 200.00, 500.00)

    conta1.deposita(50)
    conta2.transfere_para(conta1,50)
    conta1.extrato()
    conta2.extrato()
    conta1.saca(50)
    conta1.saca(10)
    conta1.historico.imprime()

