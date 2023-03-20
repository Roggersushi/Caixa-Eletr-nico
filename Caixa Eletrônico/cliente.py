class Cliente:
    def __init__(self,nome,sobrenome,cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def extrato(self):
        print(f'O nome do cliente é: {self.nome} Sobrenome: {self.sobrenome} e cpf :{self.cpf}')