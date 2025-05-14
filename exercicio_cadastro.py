clientes = []

def dados_dos_clientes():
    nome = input("nome do cliente")
    cpf = int(input("CPF"))
    RG = int(input("RG do cliente"))
    nascimento = int(input("data de nascimento"))
    CEP = int(input("endereço"))
    telefone = int(input("numero de telefone")) 
    email = int(input("digite seu email"))
    

    clientes = {
        "nome": nome,
        "cpf": cpf,
        "RG": RG,
        "nascimento": nascimento, 
        "CEP": CEP, 
        "telefone": telefone,
        "email": email
    }

    return clientes
def cadastrar_cliente(dados_dos_clientes):
    clientes.append(dados_dos_clientes)

    return clientes
def mostrar_dados_do_cliente(dados_dos_clientes):
    for clientes in dados_dos_clientes:
        print(f"""
             nome do cliente : {clientes["nome do cliente"]}")
             CPF do cliente : {clientes["nome do cliente"]}")
             RG do cliente : {clientes["nome do cliente"]}")
             Data de Nascimento do cliente : {clientes["nome do cliente"]}")
             endereco do cliente : {clientes["nome do cliente"]}")
             do cliente : {clientes["nome do cliente"]}")
             nome do cliente : {clientes["nome do cliente"]}")
             nome do cliente : {clientes["nome do cliente"]}")
             nome do cliente : {clientes["nome do cliente"]}")
             nome do cliente : {clientes["nome do cliente"]}") 
""")
        
def iniciar_sistema():
    while True:
        print("")
        print("=")*60
        print("opcao 1 - mostrar lista")
        print("opcao 2 - cadastrar clientes")
        print("opcao 3 - sair")
        print("="*80)

        opcao = input("escolha uma das opcoes do menu")

        if opcao == "1":
            mostrar_dados_do_cliente(clientes)
        elif opcao == "2":
            cadastrar_cliente(dados_dos_clientes())
        elif opcao == "3":
            print("sistema finalizado!")
            break
        else:
            print("opcao invalida, escolha uma das opcoes no menu.")





iniciar_sistema()




































































































