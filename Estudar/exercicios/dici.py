# Dicionário vazio
dicionario_vazio = {}

# Dicionário com elementos
dicionario = {'nome': 'Alice', 'idade': (26, 29), 'cidade': 'São Paulo'}

print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())

print(dicionario.get('idade'))
print(dicionario.get('ender', 'fnaof'))

dicionario['profissao'] = 'Ti'

print(dicionario.get('profissao', None))
print(dicionario.pop('profissao'))
print(dicionario.get('profissao', None))

print(dicionario['idade'])
dicionario.update({'idade': 33})
print(dicionario['idade'])