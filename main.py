import textwrap

def menu():
    """Exibe o menu de operações do sistema bancário."""
    menu_texto = """\n
    ====== ESCOLHA UMA OPERAÇÃO ========
    [d] Depositar Valor
    [s] Sacar Valor
    [e] Consultar Extrato
    [cu] Criar Usuário
    [ac] Abrir Conta
    [lc] Listar Contas
    [x] Encerrar Operação
    >>  """
    return input(textwrap.dedent(menu_texto))

def depositar(saldo, valor, extrato):
    """Realiza um depósito na conta."""
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nErro! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Realiza um saque na conta dentro dos limites estabelecidos."""
    if valor > saldo:
        print("\nErro! Saldo insuficiente.")
    elif valor > limite:
        print("\nErro! Valor excede o limite de saque.")
    elif numero_saques >= limite_saques:
        print("\nErro! Número máximo de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nErro! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    """Exibe o extrato da conta."""
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for item in extrato:
            print(item)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=========================================")

def criar_usuario(usuarios):
    """Cria um novo usuário se o CPF não estiver cadastrado."""
    cpf = input("Digite seu CPF (somente números): ")
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("\nErro! CPF já cadastrado.")
        return
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu endereço (Rua, Nº - Bairro - Cidade/UF): ")
    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    print("\nUsuário criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios, contas):
    """Cria uma nova conta para um usuário existente."""
    cpf = input("Informe o CPF do titular: ")
    usuario = next((user for user in usuarios if user["cpf"] == cpf), None)
    if usuario:
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "titular": usuario["nome"]})
        print("\nConta criada com sucesso!")
    else:
        print("\nErro! Usuário não encontrado.")

def listar_contas(contas):
    """Lista todas as contas cadastradas."""
    if not contas:
        print("\nNenhuma conta cadastrada.")
    else:
        for conta in contas:
            print("=" * 40)
            print(f"Agência: {conta['agencia']}\nConta: {conta['numero_conta']}\nTitular: {conta['titular']}")
            print("=" * 40)

def main():
    """Função principal que controla o fluxo do sistema bancário."""
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "cu":
            criar_usuario(usuarios)
        elif opcao == "ac":
            criar_conta(AGENCIA, len(contas) + 1, usuarios, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "x":
            print("Encerrando o sistema bancário.")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
