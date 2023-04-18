from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
  def __init__(self, endereco):
    self.endereco = endereco
    self.contas = []

  def realizar_transacao(self, conta, transacao):
    transacao.registrar(conta)

  def adicionar_conta(self, conta):
    self.contas.append(conta)

  def __str__(self):
    return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class PessoaFisica(Cliente):
  def __init__(self,cpf,nome,data_nascimento, endereco):
    super().__init__(endereco)
    self.cpf=cpf
    self.nome=nome
    self.data_nascimento=data_nascimento
  
  # def __del__(self):
  #   print(f'Removendo instancia da classe {self.__class__.__name__}')


class Transacao(ABC):
  @property
  @abstractproperty
  def valor(self):
    pass

  @abstractclassmethod
  def registrar(self, conta):
    pass

class Saque(Transacao):
  def __init__(self, valor):
    self._valor = valor

  @property
  def valor(self):
    return self._valor

  def registrar(self, conta):
    sucesso_transacao = conta.sacar(self.valor)
    if sucesso_transacao:
      conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
  def __init__(self, valor):
    self._valor = valor

  @property
  def valor(self):
      return self._valor

  def registrar(self, conta):
    sucesso_transacao = conta.depositar(self.valor)
    if sucesso_transacao:
      conta.historico.adicionar_transacao(self)

class Historico:
  def __init__(self):
    self._transacoes = []

  @property
  def transacoes(self):
    return self._transacoes

  def adicionar_transacao(self, transacao):
    now = datetime.now()
    data = now.strftime('%m/%d/%Y, %H:%M:%S')
    self._transacoes.append(
      {
        "tipo": transacao.__class__.__name__,
        "valor": transacao.valor,
        "data": data,
      }
    )

class Conta():
  def __init__(self,numero_conta,cliente):
    self._saldo=0.0
    self._numero_conta=numero_conta
    self._cliente=cliente
    self._historico = Historico()

  @classmethod
  def nova_conta(cls, numero_conta, cliente):
    return cls(numero_conta, cliente)

  @property
  def saldo(self):
    return self._saldo

  @property
  def numero_conta(self):
    return self._numero_conta

  @property
  def cliente(self):
    return self._cliente

  @property
  def historico(self):
    return self._historico

  def depositar(self,valor):
    if valor>0:
      self._saldo+=valor
      print('\ndeposito realizado')
      return True
    else:
      print('valor inadequado para deposito')
      return False

  def sacar(self,valor):
    if valor<=0:
      print('valor invalido para saque')
    elif self._saldo<valor:
      print('falta de saldo na conta')
    else:
      self._saldo-=valor
      return True
    return False

class ContaCorrente(Conta):
  def __init__(self, numero_conta, cliente, limite=500.0, limite_saques=3):
    super().__init__(numero_conta, cliente)
    self._limite = limite
    self._limite_saques = limite_saques

  def sacar(self, valor):
    numero_saques = len(
      [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
    )
    if valor>self._limite:
      print(f'\nlimite do valor para saque ultrapassa o limite diario de R${self._limite:.2f}')
    elif numero_saques>=self._limite_saques:
      print(f'\nlimite de saques diarios atigido: {self._limite_saques}')
    else:
      return super().sacar(valor)
    return False

  def __str__(self):
    return f" C/C:{self.numero_conta}"

class Agencia():
  def __init__(self,numero_agencia):
    self.AGENCIA = numero_agencia
    self.clientes = []
    self.contas = []

  def filtrar_cliente(self, cpf):
    clientes_filtrados = [cliente for cliente in self.clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

  def criar_cliente(self):
    cpf = input("Informe o CPF (somente numeros): ")
    cliente = self.filtrar_cliente(cpf)

    if cliente:
        print("\nExiste cliente cadastrado com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    cliente=PessoaFisica(cpf=cpf,nome=nome,data_nascimento=data_nascimento,endereco=endereco)
    self.clientes.append(cliente)
    print("\n=== Cliente criado com sucesso! ===")

  def listar_clientes(self):
    for cliente in self.clientes:
      clientestr="Cliente: cpf={cpf}, nome={nome}, data_nascimento={niver}, endereço={end}, ".format(end=cliente.endereco, cpf=cliente.cpf, nome=cliente.nome, niver=cliente.data_nascimento)
      contastr=''
      for conta in cliente.contas:
        linha = "Agência: {ag} C/C: {cc}".format(ag=self.AGENCIA,cc=conta.numero_conta)
        contastr+=f'{linha},'
      clientestr+=f'contas=[{contastr}]'
      print("=" * 100)
      print(clientestr)

  def criar_conta(self):
    cpf = input("Informe o CPF do cliente: ")
    cliente = self.filtrar_cliente(cpf)
    if cliente:
      numero_conta = len(self.contas) + 1
      conta = ContaCorrente.nova_conta(numero_conta=numero_conta, cliente=cliente)
      self.contas.append(conta)
      cliente.contas.append(conta)
      print("\n=== Conta criada com sucesso! ===")
    else:
      print("\nCliente nao encontrado, fluxo de criacao de conta encerrado!")

  def listar_contas(self):
    for conta in self.contas:
        linha = f"Agência:\t{self.AGENCIA} C/C:\t\t{conta.numero_conta} Titular:\t{conta.cliente.nome}"
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
  
  def depositar(self,conta):
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    conta.cliente.realizar_transacao(conta, transacao)

  def sacar(self,conta):
    valor = float(input("Informe o valor para saque: "))
    transacao = Saque(valor)
    conta.cliente.realizar_transacao(conta, transacao)

  def exibir_extrato(self,conta):
    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes
    extrato = ""
    if not transacoes:
      extrato = "Não foram realizadas movimentações."
    else:
      for transacao in transacoes:
        extrato += f"\n{transacao['tipo']}:\n{transacao['data']}\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

def main():
  menu_agencia = """\n
    ================ MENU AG ================
    [nc]\tNova conta
    [lc]\tListar contas
    [sc]\tSelecionar conta
    [nu]\tNovo Cliente
    [lu]\tListar clientes
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
        agencia.criar_cliente()
      elif opcao == "nc":
        agencia.criar_conta()
      elif opcao == "lc":
        agencia.listar_contas()
      elif opcao == "lu":
        agencia.listar_clientes()
      elif opcao=='q':
        break
      else:
        print('opcao invalida, tente novamente')
    else:
      opcao=input(menu_conta)
      if opcao=='d':
        agencia.depositar(conta)
      elif opcao=='s':
        agencia.sacar(conta)
      elif opcao=='e':
        agencia.exibir_extrato(conta)
      elif opcao=='v':
        conta=None
      else:
        print('opcao invalida, tente novamente')

main()
