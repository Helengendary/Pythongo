# Autoras: Raissa Queiroz e Helena Picinin

import json

class User():
  def __init__(self, name, password, status, ler, escrever, deletar):
    self.name = name
    self.passw = password
    self.stt = status
    self.ler = ler
    self.escrever = escrever
    self.deletar = deletar

  def Login(self, nameEnter, passwordEnter):
    if nameEnter == self.name and passwordEnter == self.passw:
      return True
    else:
      return False

  def SignUp(self, users):
    users.append({'name': self.name, 'passw': self.passw, 'status': self.stt, 'ler': self.ler, 'escrever': self.escrever, 'deletar': self.deletar})
    with open('user.json', 'w', encoding='utf-8') as arquivo:
      json.dump(users, arquivo)

  def Forbidden(self, users):
      for user in users:
        if user['name'] == self.name:
          user['status'] = False
          print("Usuário Bloqueado!")
          break
      with open('user.json', 'w', encoding='utf-8') as arquivo:
        json.dump(users, arquivo)

try:
  with open('user.json', 'r', encoding='utf-8') as arquivo:
    data_json = json.load(arquivo)
except json.JSONDecodeError:
  data_json = []

menu = int(input("MENU:\n1 - Cadastrar\n2 - Entrar\nr:"))
atual = User("", "", True, [], [], [])

match menu:
  case 1:
    print("\n================================\nCADASTRO\n")
    nameIn = input("Name:")
    passIn = input("Pass:")

    print("\n================================") 
    ler = input('Quais documentos você quer ter acesso para LER?\nariana.mp3\npaçoca.jpg\nuser.json\nOBS: Escreva em letras minúsculas e com vírgulas ex:1.jpg, 2,mp3\nr: ')
    ler = ler.split(', ')

    print("\n================================") 
    escrever = input('\n\nQuais documentos você quer ter acesso para ESCREVER?\nariana.mp3\npaçoca.jpg\nuser.json\nOBS: Escreva em letras minúsculas e com vírgulas ex:1.jpg, 2,mp3\nr: ')
    escrever = escrever.split(', ')

    print("\n================================") 
    deletar = input('\n\nQuais documentos você quer ter acesso para ESCREVER?\nariana.mp3\npaçoca.jpg\nuser.json\nOBS: Escreva em letras minúsculas e com vírgulas ex:1.jpg, 2,mp3\nr: ')
    deletar = deletar.split(', ')

    user = User(nameIn, passIn, True, ler, escrever, deletar)
    user.SignUp(data_json)
    atual = user

    print("\n================================") 
    print(f"\nSeja bem vindo, {atual.name}\n")
  case 2:
    tries = 1
    sucess = False
    exists = False
    while tries <= 5:

      print("\n================================\nENTRAR\n")
      nameIn = input("Name:")
      passIn = input("Pass:")

      for user in data_json:
        analise = User(user["name"], user['passw'], user["status"], user["ler"], user["escrever"], user["deletar"])

        if (analise.Login(nameIn, passIn)):
          tries = 6
          if (not user["status"]):
            print("\nUsuário bloqueado\n")
            break
          sucess = True
          break

        if (analise.name == nameIn):
          exists = True

        if (exists and (not sucess) and tries == 5):
          analise.Forbidden(data_json)

      if (sucess):
        print(f"\n\nSeja bem vindo, {analise.name}\n")
        atual = analise
        tries = 6

      else:
        print("\nLogin ou senha incorreto. Tente novamente mais tarde.\n")

      tries+=1

while True:
  print('\n================================')
  function = int(input('FUNÇÕES\n1 - Ler\n2 - Escrever\n3 - Deletar\n0 - Sair\nr:'))

  match function:
    case 1:
      lista = atual.ler
    case 2:
      lista = atual.escrever
    case 3:
      lista = atual.deletar
    case 0:
      break
    case _:
      print('Opção inválida')
      continue

  print('\n================================')
  arquivo = input('ARQUIVOS\nariana.mp3\npaçoca.jpg\nuser.json\nOBS: Escreva em letras minúsculas\nr:')

  if(arquivo in lista and not arquivo == ''):
    print('\nTem acesso!!!')
  else:
    print('\nNão tem acesso!!!')

#   [
# 	{
# 		"nome": "nome",
# 		"senha": "senha",
# 		"status": 1,
# 		"ler": ["arq.csv", "user.json", "hdvsdh.id"],
# 		"escrever": [],
# 		"deletar": []
# 	}
# ]

