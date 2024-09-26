
############################################################

# Objetivo Geral: Separar as operações existentes do sistema em funções e criar duas novas: cadastar usuário(cliente) e criar conta corrente.

# Desafio -> Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: Sacar, Depositar e Extrato. Além disso, para a versão 2 do sistema, precisamos criar duas novas operações: cadastrar usuário (cliente) e criar conta corrente (vinculada ao cliente).

    # 1. Cada função vai ter uma regra de parâmetros/argumentos.

    # 2. O retorno e a chamada podem ser definidos do jeito que você achar melhor.

    # 3. def saque() -> A função deve recerber apenas argumentos nomeados(keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques). Sugestão de retorno -> saldo e extrato

    # 4. def depositar() -> A função deve receber apenas argumentos por posição (positional only). Sugestão de argumentos: saldo, valor, extrato). Sugestão de retorno -> saldo e extrato

    # 5. def extrato() -> A função deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados:extrato.

    # 6. Pode ser criado uma função adicional: lista de contas

    # 7. cadastrar_novo_cliente -> O programa deve armazenar os clientes em uma lista[]. Um cliente é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string (str) com o formato: logradouro - bairro - cidade/sigla. Deve ser armazenado somente os númeoros do CPF. Não podemos cadastrar 2 clientes com o mesmo CPF.

    # 8. criar_conta_corrente -> O programa deve armazenar contas em uma lista[]. Uma conta é composta por: agência, número da conta e cliente. O número da conta é sequencial, iniciado por 1. O número da agência é fixo "0001". O cliente pode ter mais de uma conta, mas uma conta pertence a somente um cliente.
    
    # Dica: Para vincular um cliente a uma conta, filtre a lista de clientes buscando o número do cpf informado para cada cliente da lista.

############################################################
# Importação de textwrap para facilitar a exibição do menu de opções
import textwrap


# Função responsável por exibir o menu de opções do sistema bancário.
def menu():
    menu_banco = """\n
    ======= MENU =======
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Cadastrar Novo Cliente
    [cc] Criar Conta Corrente
    [lc] Lista de Contas
    [q] Sair

    => """
    return input(textwrap.dedent(menu_banco))  # Exibe o menu removendo possíveis recuos de texto.

# Função de depósito: atualiza o saldo e registra a transação no extrato.
# Argumentos recebidos são somente por posição (positional-only).
def depositar(saldo_conta, valor_deposito, historico_transacoes, /):
    if valor_deposito > 0:  # Verifica se o valor do depósito é válido.
        saldo_conta += valor_deposito  # Adiciona o valor depositado ao saldo.
        historico_transacoes += f"Depósito: R$ {valor_deposito:.2f}\n"  # Registra a transação no extrato.
    else:
        print("Operação falhou! O valor informado é inválido.")  # Exibe mensagem de erro para valor inválido.
    return saldo_conta, historico_transacoes  # Retorna o saldo atualizado e o extrato.

# Função de saque: atualiza o saldo, registra o saque e faz as verificações necessárias.
# Argumentos nomeados (keyword-only).
def sacar(*, saldo_conta, valor_saque, extrato, limite_saque, qtd_saques_realizados, qtd_saques_diarios_possiveis):
    saldo_insuficiente = valor_saque > saldo_conta  # Verifica se o saldo é suficiente para o saque.
    saque_acima_do_limite = valor_saque > limite_saque  # Verifica se o saque ultrapassa o limite diário.
    saques_diarios_excedidos = qtd_saques_realizados >= qtd_saques_diarios_possiveis  # Verifica se já excedeu o limite de saques diários.

    if saldo_insuficiente:
        print("Operação falhou! Você não tem saldo suficiente.")  # Saldo insuficiente.
    elif saque_acima_do_limite:
        print("Operação falhou! O valor do saque excede o limite.")  # Saque acima do limite diário permitido.
    elif saques_diarios_excedidos:
        print("Operação falhou! Número máximo de saques excedido.")  # Excedeu o limite de saques diários.
    elif valor_saque > 0:
        saldo_conta -= valor_saque  # Deduz o valor do saque do saldo.
        extrato += f"Saque: R$ {valor_saque:.2f}\n"  # Registra o saque no extrato.
        qtd_saques_realizados += 1  # Incrementa o contador de saques realizados.
    else:
        print("Operação falhou! O valor informado é inválido.")  # Valor de saque inválido.
    return saldo_conta, extrato  # Retorna o saldo atualizado e o extrato.

# Função que exibe o extrato de transações e o saldo da conta.
# Argumentos posicionais e nomeados.
def exibir_extrato(saldo_conta, /, *, extrato):
    print("\n================ EXTRATO ================")
    # Verifica se há transações e exibe o extrato ou uma mensagem de "sem movimentações".
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo_conta:.2f}")
    print("==========================================")

# Função para cadastrar novos clientes.
def cadastrar_novo_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_clientes(cpf, clientes)  # Verifica se o cliente já existe.

    if cliente:
        print("\nJá existe cliente com esse CPF!")  # Verifica se o CPF já foi cadastrado.
        return

    # Coleta as informações do cliente e o adiciona à lista de clientes.
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Cliente criado com sucesso! ===")

# Função que filtra os clientes por CPF.
def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]  # Filtra a lista de clientes pelo CPF.
    return clientes_filtrados[0] if clientes_filtrados else None  # Retorna o cliente, se encontrado.

# Função para criar contas correntes, vinculando ao cliente.
def criar_conta_corrente(agencia, numero_da_conta, clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)  # Busca o cliente pelo CPF.

    if cliente:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_da_conta, "cliente": cliente}  # Cria a conta vinculada ao cliente.

    print("\n Cliente não encontrado, fluxo de criação de conta encerrado!")

# Função que exibe a lista de contas correntes cadastradas.
def criar_lista_contas(contas):
    for conta in contas:
        linha = f"""\  
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['cliente']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))  # Exibe os detalhes da conta.

# Função principal que implementa o fluxo do sistema bancário.
def main():
    QTD_SAQUES_DIARIOS_POSSIVEIS = 3  # Limite diário de saques.
    AGENCIA = "0001"

    saldo_conta = 0  # Saldo inicial da conta.
    limite_saque = 500  # Limite de saque por transação.
    extrato = ""  # Histórico de transações.
    qtd_saques_realizados = 0  # Contador de saques realizados.
    clientes = []  # Lista de clientes.
    contas = []  # Lista de contas correntes.

    while True:
        opcao_menu = menu()  # Exibe o menu e recebe a opção selecionada pelo usuário.

        if opcao_menu == "d":
            valor_deposito = float(input("Informe o valor do depósito: "))  # Recebe o valor do depósito.
            saldo_conta, extrato = depositar(saldo_conta, valor_deposito, extrato)  # Executa o depósito.

        elif opcao_menu == "s":
            valor_saque = float(input("Informe o valor do saque: "))  # Recebe o valor do saque.
            saldo_conta, extrato = sacar(
                saldo_conta=saldo_conta,
                valor_saque=valor_saque,
                extrato=extrato,
                limite_saque=limite_saque,
                qtd_saques_realizados=qtd_saques_realizados,
                qtd_saques_diarios_possiveis=QTD_SAQUES_DIARIOS_POSSIVEIS,
            )

        elif opcao_menu == "e":
            exibir_extrato(saldo_conta, extrato=extrato)  # Exibe o extrato.

        elif opcao_menu == "nc":
            cadastrar_novo_cliente(clientes)  # Cadastra um novo cliente.

        elif opcao_menu == "cc":
            numero_conta = len(contas) + 1  # Gera o número da conta.
            conta = criar_conta_corrente(AGENCIA, numero_conta, clientes)  # Cria a conta corrente.

            if conta:
                contas.append(conta)  # Adiciona a nova conta à lista de contas.

        elif opcao_menu == "lc":
            criar_lista_contas(contas)  # Exibe a lista de contas cadastradas.

        elif opcao_menu == "q":
            break  # Encerra o programa.

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")  # Mensagem de erro para opções inválidas.

# Inicia o programa chamando a função main.
main()