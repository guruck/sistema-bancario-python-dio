class Conta():
  def __init__(self):
    self.LIMITE_VALOR_SAQUE=500.0
    self.LIMITE_QUANTIDADE_SAQUE=3
    self.saldo=0.0
    self.extrato=''
    self.numero_de_saques=0

  def __str__(self):
        return f'{self.extrato}\nSaldo: R$ {self.saldo:.2f}'

  def depositar(self):
    valor = input('digite o valor depositado ->')
    if str(valor).isdecimal:
      aux=float(valor)
      if aux>0:
        self.saldo+=aux
        self.extrato+=f'R$ {aux:.2f} D\n'
      else:
        print('valor invalido para deposito')
    else:
      print('digite valor adequado para deposito')

  def sacar(self):
    valor = input('digite o valor para saque ->')
    if str(valor).isdecimal:
      aux=float(valor)
      if aux<=0:
        print('valor invalido para deposito')
      elif self.saldo<=aux:
        print('falta de saldo na conta')
      elif aux>self.LIMITE_VALOR_SAQUE:
        print(f'limite do valor para saque ultrapassa o limite diario de R${self.LIMITE_VALOR_SAQUE:.2f}')
      elif self.numero_de_saques>=self.LIMITE_QUANTIDADE_SAQUE:
        print(f'limite de saques diarios atigido: {self.LIMITE_QUANTIDADE_SAQUE}')
      else:
        self.saldo-=aux
        self.extrato+=f'R$ {aux:.2f} S\n'
        self.numero_de_saques+=1
    else:
      print('digite valor adequado para saque')


menu='''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''


conta= Conta()
while True:
    opcao=input(menu)
    if opcao=='d':
        conta.depositar()
    elif opcao=='s':
        conta.sacar()
    elif opcao=='e':
        print(conta)
    elif opcao=='q':
        break
    else:
        print('opcao invalida, tente novamente')