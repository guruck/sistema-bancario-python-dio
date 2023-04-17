class Agencia():
  def __init__(self,numero):
    self.AGENCIA = numero
    self.usuarios = []
    self.contas = []

  def criar_conta(self):
    cpf = input("Informe o CPF do usuario: ")
    usuario = self.filtrar_usuario(cpf)
    if usuario:
      numero_conta = len(self.contas) + 1
      conta = Conta(numero_conta, usuario)
      self.contas.append(conta)
      print("\n=== Conta criada com sucesso! ===")
    else:
      print("\nUsuario nao encontrado, fluxo de criacao de conta encerrado!")

  def listar_contas(self):
    for conta in self.contas:
        linha = f"Agência:\t{self.AGENCIA} C/C:\t\t{conta.numero_conta} Titular:\t{conta.usuario.nome}"
        print("=" * 100)
        print(linha)

  def selecionar_conta(self):
    numero_conta = input("Informe o numero da conta (somente numeros): ")
    if str(numero_conta).isdecimal:
      if (int(numero_conta) > 0 ):
        conta_filtrada = [conta for conta in self.contas if conta.numero_conta == int(numero_conta)]
        return conta_filtrada[0] if conta_filtrada else None
    else:
       print('Informe um numero inteiro válido')
       return None

  def criar_usuario(self):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = self.filtrar_usuario(cpf)

    if usuario:
        print("\nExiste usuario cadastrado com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    cliente=Usuario(cpf=cpf,nome=nome,data_nascimento=data_nascimento)
    self.usuarios.append(cliente)
    print("=== Usuário criado com sucesso! ===")

  def filtrar_usuario(self, cpf):
    usuarios_filtrados = [usuario for usuario in self.usuarios if usuario.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
  
  def listar_usuarios(self):
    for usuario in self.usuarios:
        print("=" * 100)
        print(usuario)

class Conta():
  def __init__(self,numero_conta,usuario):
    self.LIMITE_VALOR_SAQUE=500.0
    self.LIMITE_QUANTIDADE_SAQUE=3
    self._saldo=0.0
    self.extrato=''
    self.numero_de_saques=0
    self.numero_conta=numero_conta
    self.usuario=usuario

  def __str__(self):
        extrato_aux = "Não foram realizadas movimentações." if self.extrato == ''  else self.extrato
        return f'{extrato_aux}\nSaldo: R$ {self._saldo:.2f}'

  def depositar(self):
    valor = input('digite o valor depositado ->')
    if str(valor).isdecimal:
      aux=float(valor)
      if aux>0:
        self._saldo+=aux
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
        print('valor invalido para saque')
      elif self._saldo<aux:
        print('falta de saldo na conta')
      elif aux>self.LIMITE_VALOR_SAQUE:
        print(f'limite do valor para saque ultrapassa o limite diario de R${self.LIMITE_VALOR_SAQUE:.2f}')
      elif self.numero_de_saques>=self.LIMITE_QUANTIDADE_SAQUE:
        print(f'limite de saques diarios atigido: {self.LIMITE_QUANTIDADE_SAQUE}')
      else:
        self._saldo-=aux
        self.extrato+=f'R$ {aux:.2f} S\n'
        self.numero_de_saques+=1
    else:
      print('digite valor adequado para saque')

class Usuario():
  def __init__(self,cpf,nome,data_nascimento):
    self.cpf=cpf
    self.nome=nome
    self.data_nascimento=data_nascimento
  
  def __del__(self):
    print(f'Removendo instancia da classe {self.__class__.__name__}')

  def __str__(self):
    return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

def main():
  menu_agencia = """\n
    ================ MENU AG ================
    [nc]\tNova conta
    [lc]\tListar contas
    [sc]\tSelecionar conta
    [nu]\tNovo usuario
    [lu]\tListar usuarios
    [q] \tSair
    => """
  
  menu_conta = """\n
    ================ MENU CC ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [v]\tSair da Conta
    => """

  agencia = Agencia('0001')
  conta=None
  while True:
    if conta is None:
      opcao= input(menu_agencia)
      if opcao=="sc":
        conta=agencia.selecionar_conta()
      elif opcao == "nu":
        agencia.criar_usuario()
      elif opcao == "nc":
        agencia.criar_conta()
      elif opcao == "lc":
        agencia.listar_contas()
      elif opcao == "lu":
        agencia.listar_usuarios()
      elif opcao=='q':
        break
      else:
        print('opcao invalida, tente novamente')
    else:
      opcao=input(menu_conta)
      if opcao=='d':
        conta.depositar()
      elif opcao=='s':
        conta.sacar()
      elif opcao=='e':
        print(conta)
      elif opcao=='v':
        conta=None
      else:
        print('opcao invalida, tente novamente')


main()