
def novo_usuario(usuarios):
     cpf= input("Informe o CPF (apenas números): ")
     usuario = filtro_de_usuario(cpf, usuarios)

     if usuario:
          print("Usuario já existente")
          return
     nome = input("Digite o nome completo: ")
     nascimento = input("Informe a data de nascimento (dia/mês/ano): ")
     endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla do estado): ")
     usuarios.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})
     print("Novo usuário criado com sucesso!")


def filtro_de_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None


def nova_conta(agencia, numero_conta, usuarios):
     cpf = input("Informe o CPF: ")
     usuario = filtro_de_usuario(cpf, usuarios)
     if usuario:
          print("\nConta criada com sucesso!")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
     print ("Usuário não encontrado! Criação de conta encerrada!")


def depositar(saldo, valor, extrato, /):
    if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
                Print("\nDeposito realizado!")

    else:
        print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def extrato_em_conta(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")






menu = """
      ~~~~ MENU INICIAL ~~~~
[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usuário
[5] Nova Conta
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = sacar(
             saldo=saldo,
             valor=valor,
             extrato=extrato,
             limite=limite,
             numero_saques=numero_saques,
             limite_saques=LIMITE_SAQUES,
        )

    elif opcao == "3":
        extrato_em_conta(saldo, extrato=extrato)

    elif opcao == "4":
        novo_usuario(usuarios)

    elif opcao == "5":
        numero_conta = len(contas) + 1
        conta = nova_conta(AGENCIA, numero_conta, usuarios)
        if conta:
             contas.append(conta)
                      
    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")