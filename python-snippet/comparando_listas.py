lista = ['a', 'b', 'c']
lista_full = ['a', 'b', 'c', 'd', 'e']

lista_final = [x for x in lista_full if x not in lista]

print(lista)
print(lista_full)
print(lista_final)
