from conta import*
from cliente import*

if __name__ == '__main__':
    cliente = Cliente('Fabrici', 'Dias', 12507830401)
    conta1 = Conta('123-5', cliente,120.00, 500.00)
    conta2 = Conta('234-5', 'Debora Firmiano', 200.00, 500.00)

    print(type(conta1.numero))
    print(type(conta1.titular))
    print(type(conta1.limite))




