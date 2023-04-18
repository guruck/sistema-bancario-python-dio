# sistema-bancario-python-dio
desafio de criacao do sistema bancario

## Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45

## Evolução - desafio 02
Proposto organizar as transações com funções definidas bem como algumas outras regras
(plus) Implementado a troca de menus de acordo com a funcionalidade para conta ou agencia

## Evolução - desafio_poo
Proposto organizar o projeto seguindo paradigma de orientação a objetos
Foi realizado o ajuste do modelo proposto para adequar a evolução anterior, aproveitando a entidade "Agência" dado que o main fica bem largado na proposta original
(plus) aqui além de toda melhoria já implementada desde o desafio original, temos uma estrutura de menus adequadas e o controle por conta e não pelo cliente. Na proposta original o controle busca a conta atrelada no cliente e o cliente não tem opção de escolher qual das contas vai depositar

(ponto de melhoria) o cliente se identificar no sistema e escolher apenas dentre suas contas