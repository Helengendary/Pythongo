import ttg

print("Lista de Exercício 1\n")

print(ttg.Truths(['p'], ['~p'], ints=False))
print('\n')

print(ttg.Truths(['p', 'q'], ['p and q'], ints=False))
print('\n')

print(ttg.Truths(['p', 'q'], ['p or q'], ints=False))
print('\n')

print(ttg.Truths(['p', 'q'], ['p = q'], ints=False))
print('\n')

print(ttg.Truths(['p', 'q'], ['p => (~q)'], ints=False))
print('\n')

print(ttg.Truths(['p', 'q'], ['p or (~q)'], ints=False))
print('\n')

print(ttg.Truths(['p', 'q'], ['(~p) and (~q)'], ints=False))
print('\n')

print(ttg.Truths(['p', 'q'], ['p = (~q)'], ints=False))
print('\n')

print(ttg.Truths(['p', 'q'], ['(p and (~q)) => p'], ints=False))
print('\n')



print('lista 2 - Exercicio 3\n')

print(ttg.Truths(['a', 'b'], ['(~a) and b']))
print('\n')

print(ttg.Truths(['a', 'b'], ['(~b) => (a or b)']))
print('\n')

print(ttg.Truths(['a', 'c'], ['(c or a) = (~(~c))']))
print('\n')

print(ttg.Truths(['a', 'b'], ['a or (a => b)']))
print('\n')

print(ttg.Truths(['a', 'd', 'c'], ['(d or (~a))=>(~c)']))
print('\n')

print(ttg.Truths(['a', 'b', 'c'], ['(~(a and b))=>(~(c and b))']))
print('\n')

print('lista 2 - Exercicio 4')

print(ttg.Truths(['p', 'q'], ['~(p=>(~q)) ']))
print('\n')

print(ttg.Truths(['p', 'q', 'r'], ['p = (~q) and r ']))
print('\n')

print(ttg.Truths(['p', 'q'], ['p=>(~q) and p or q = p or (~q)']))
print('\n')



print('Lista 3\n')

print(ttg.Truths(['t', 'd', 'l'], ['(t and d) and l']))
print('\n')

print(ttg.Truths(['m']))
print('\n')

print(ttg.Truths(['a', 'b', 'r'], ['a and(b or r)']))
print('\n')

print(ttg.Truths(['m', 'r'], ['m and r']))
print('\n')

print(ttg.Truths(['a', 'h', 't'], ['(a and h) or (t or (~h))']))
print('\n')