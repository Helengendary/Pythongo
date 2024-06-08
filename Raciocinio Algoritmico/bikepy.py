nome_usuarios = ["Helena", "Ana", "Raissa"]
senha_usuarios = ["1234", "5678", "91011"]
verifica_usuario = False
verifica_senha = False
index_senha = ""
index_usuario = ""
contador_login = 0

Entrada = False

while True:

    if contador_login > 0:
        continuar = int(input("0 - sair\n1 - Tentar novamente\n"))
        if continuar == 0:
            break

    usuario_entrada = input("\nDigite o nome de usuário:\n")
    senha_entrada = input("\nSenha:\n")

    for i in nome_usuarios:

        if i == usuario_entrada:
            index_usuario = nome_usuarios.index(i)
            verifica_usuario = True
            break

    for i in senha_usuarios:

        if i == senha_entrada:
            index_senha = senha_usuarios.index(i)
            verifica_senha = True
            break


    if not verifica_usuario:
        if not verifica_senha:
            print("\nUsuário e senha inválidos!\n")
        else:
            print("\nUsuário inválido!\n")
    else: 
        if index_usuario == index_senha:
            Entrada = True
            break
        else:
            print("\nSenha incorreta!\n")

    contador_login += 1

while Entrada:
    break