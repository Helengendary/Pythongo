import datetime

# Vetor
nome_usuarios = ["helena", "ana", "raissa"]
id_usuarios = [1, 2, 3]
senha_usuarios = ["1234", "5678", "91011"]
creditos_usuarios = [100, 200, 300]
relatorios_usuarios = {1: [], 2: [], 3: []}

# Variáveis
verifica_usuario = False # Flag para verificar se o nome de usuário é válido
verifica_senha = False # Flag para verificar se a senha de usuário é válido
id_usuario_logado = 0 # Verifica qual usuário está logado
index_senha = "" # Salva o valor do index da lista usuário
index_usuario = "" # Salva o valor do index da lista senhas
contador_login = 0 # Contador para quantas vezes o login foi feito

Entrada = False # Autoriza ao sistema se o usuário e a senha estiverem certos

# Funções

def ver_creditos(id_usuario_logado):
    indice = id_usuarios.index(id_usuario_logado)  # Encontra o índice do usuário pelo ID
    print(f"----- Você tem {creditos_usuarios[indice]} créditos -----")

def adicionar_creditos(id_usuario_logado, valor):
    indice = id_usuarios.index(id_usuario_logado)
    creditos_usuarios[indice] += valor # Adiciona o valor de crédito ao usuário
    data_hora_atual = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    relatorios_usuarios[id_usuario_logado].append(f"----- {data_hora_atual} - Adicionado {valor} créditos -----")
    print(f"{valor} créditos adicionados. Você agora tem {creditos_usuarios[indice]} créditos.")

def remover_creditos(id_usuario_logado, valor):
    indice = id_usuarios.index(id_usuario_logado) # Encontra o índice do usuário pelo ID

    # Verifica se o usuário tem créditos o suficiente
    if creditos_usuarios[indice] >= valor:
        creditos_usuarios[indice] -= valor # Remove o valor de créditos do usuário
        data_hora_atual = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") #Operação de relatório
        relatorios_usuarios[id_usuario_logado].append(f"----- {data_hora_atual} - Removido {valor} créditos -----")
        print(f"{valor} créditos removidos. Você agora tem {creditos_usuarios[indice]} créditos.")
    else:
        print("Créditos insuficientes.")

def gerar_relatorio(id_usuario_logado):
    print("\nRelatório de uso:\n")

    # Verifica  se possui algum registro
    if relatorios_usuarios[id_usuario_logado] == []:
        print("Realize alguma operação dentro do aplicativo para que possa gerar um relatório de uso")

    # Imprime o histórico de acordo com o usuário logado
    for registro in relatorios_usuarios[id_usuario_logado]:
        print(registro)

    data_hora_atual = datetime.datetime.now().strftime("%d-%m-%Y às %H:%M:%S")
    print(f"\nRelatório gerado dia {data_hora_atual}.\n")

def ultilizar_creditos(id_usuario_logado):
    indice = id_usuarios.index(id_usuario_logado) # Encontra o índice do usuário pelo ID

    creditos_ultilizados = int(input("Quantos créditos deseja ultilizar: "))

    # Verifica se a pessoa possui mais de 5 créditos
    if creditos_usuarios[indice] >= creditos_ultilizados*5:

        # Diminui a quantidade de créditos ultilizados
        creditos_usuarios[id_usuarios.index(id_usuario_logado)] -= creditos_ultilizados*5

        hora_atual = datetime.datetime.now()
        nova_hora = hora_atual + datetime.timedelta(hours=creditos_ultilizados)
        print("Você tem até ", nova_hora.strftime("%Y-%m-%d %H:%M:%S"), "para usar o bicicleta") # Avisa até que horas a pessoa vai poder usar a bicicleta
        data_hora_atual = datetime.datetime.now().strftime("%d-%m-%Y às %H:%M:%S")
        relatorios_usuarios[id_usuario_logado].append(f"----- {data_hora_atual} - Ultilizados {creditos_ultilizados} créditos -----")
    else:
        print("Saldo insuficiente!")


# Principal
while True:

    # verifica se a pessoa precisa entrar denovo
    if contador_login > 0:
        continuar = int(input("0 - Sair\n1 - Entrar\n"))
        if continuar == 0:
            break

    # Autenticação      
    usuario_entrada = input("\nDigite o nome de usuário:\n").lower()
    senha_entrada = input("\nSenha:\n").lower()

    # Procura se o usuário inserido existe
    for i in nome_usuarios:
        if i == usuario_entrada:
            index_usuario = nome_usuarios.index(i)
            id_usuario_logado = id_usuarios[index_usuario]
            verifica_usuario = True
            break

    # Verifica se a senha pertence ao usuário
    for i in senha_usuarios:
        if i == senha_entrada:
            index_senha = senha_usuarios.index(i)
            verifica_senha = True
            break

    # Verifica se é só o usuário está errado ou a senha também
    if not verifica_usuario:
        if not verifica_senha:
            print("\nUsuário e senha inválidos!\n")
        else:
            print("\nUsuário inválido!\n")

    # Finalização da Autenticação

    else:

        # Verifica se a senha corresponde ao usuário
        if index_usuario == index_senha:
            Entrada = True
            while Entrada: # Menu de opções
                print("\nSelecione a opção desejada:") 
                print("1 - Ver Créditos")
                print("2 - Adicionar Créditos")
                print("3 - Remover Créditos")
                print("4 - Gerar Relatório")
                print("5 - Ultilizar Créditos")
                print("0 - Sair do usuário")
                opcao = int(input("Opção: "))

                if opcao == 1:
                    ver_creditos(id_usuario_logado)
                elif opcao == 2:
                    valor = int(input("Digite o valor de créditos a adicionar: "))
                    adicionar_creditos(id_usuario_logado, valor)
                elif opcao == 3:
                    valor = int(input("Digite o valor de créditos a remover: "))
                    remover_creditos(id_usuario_logado, valor)
                elif opcao == 4:
                    gerar_relatorio(id_usuario_logado)
                elif opcao == 5:
                    ultilizar_creditos(id_usuario_logado)
                elif opcao == 0:
                    print("Saindo...")
                    Entrada = False
                else:
                    print("Opção inválida.")
        else:
            print("\nSenha incorreta!\n")

    contador_login += 1