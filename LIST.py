"""
Lista em Python
Fatiamente
append, insert, pop, del, clear, extend, +
min, max
range
"""
lista_1 = [1, 2, 3, 4, 'texto', True or False, 10.3]  # Pode guarda: Int, Float, Bool, Str, Funções, Classes

#          0    1    2    3    4
lista_2 = ['A', 'B', 'C', 'D', 'E']
#         -5   -4   -3   -2   -1

print(lista_2[1])
print(lista_2[4])
print(lista_2[-1])
print(lista_2[-1::-1], '\n')

print('Pode modificar o valor')
lista_2[1] = 'Meu nome'
print(lista_2, '\n')

print('Pode ser fazer um concatenação')
lista_3 = ['everton', 'coelho', 22]
lista_3.extend(lista_2)
lista_4 = lista_1 + lista_2
print(lista_3)
print(lista_4, '\n')

print('Pode adicionar')
lista_2.append(('RIBEIRO', 'SILVA'))  # sempre na ultima posição
lista_2.extend('SANTOS')  # add um valor de cada vez!
lista_2.insert(-1, 'LOUCOS')  # Adicione na indice desejada
print(lista_2, '\n')

print('Pode apagar valores/indices')
lista_2.pop(0)  # Posso escolher a indices
lixo = lista_2.pop()  # Usando .pop em um variavel, antes de apagar ele salva o numero na varial!
del lista_3  # Apagado a lista inteira
del lista_2[:3]  # Pode informa a indice, ou usar fatiamento
print(lixo)
print(lista_2, '\n')

print('Pegando os valores max e o min')
lista_1 = [30, 50, 1000, -1]
print(max(lista_1))
print(min(lista_1), '\n')

print('Criando uma lista com range')
list_range = list(range(0, 10))
print(list_range)

print('Fazendo copia de lista')
lista_1 = [1, 2, 3, 4, 5, 6, 7]
copia_1 = lista_1.copy()
copia_2 = [lista_1[:]]
