'''definicao da classe para controle do sistema bancario PEP8
'''


class Conta():
    '''essa classe controla as operacoes e definicoes de conta'''
    def __init__(self):
        self.limite_valor_saque = 500.0
        self.limite_quantidade_saques = 3
        self.saldo = 0.0
        self.extrato = ''
        self.numero_de_saques = 0

    def __str__(self):
        return f'{self.extrato}\nSaldo: R$ {self.saldo:.2f}'

    def depositar(self):
        '''realiza deposito de determinado valor no saldo da conta'''
        valor = input('digite o valor depositado ->')
        if valor.isdecimal:
            aux = float(valor)
            if aux > 0:
                self.saldo += aux
                self.extrato += f'R$ {aux:.2f} D\n'
            else:
                print('valor invalido para deposito')
        else:
            print('digite valor adequado para deposito')

    def sacar(self):
        '''realiza saque de determinado valor no saldo da conta'''
        valor = input('digite o valor para saque ->')
        if valor.isdecimal:
            aux = float(valor)
            if aux <= 0:
                print('valor invalido para deposito')
            elif self.saldo <= aux:
                print('falta de saldo na conta')
            elif aux > self.limite_valor_saque:
                print(f'limite do valor para saque ultrapassa o limite diario\
                       de R${self.limite_valor_saque:.2f}')
            elif self.numero_de_saques >= self.limite_quantidade_saques:
                print(f'limite de saques diarios atigido:\
                       {self.limite_quantidade_saques}')
            else:
                self.saldo -= aux
                self.extrato += f'R$ {aux:.2f} S\n'
                self.numero_de_saques += 1
        else:
            print('digite valor adequado para saque')


MENU = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''


conta = Conta()
while True:
    opcao = input(MENU)
    if opcao == 'd':
        conta.depositar()
    elif opcao == 's':
        conta.sacar()
    elif opcao == 'e':
        print(conta)
    elif opcao == 'q':
        break
    else:
        print('opcao invalida, tente novamente')
