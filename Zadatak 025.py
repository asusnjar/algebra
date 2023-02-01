# lista = list(range(1,31))

# for i in lista:
#     if i % 3 == 0:
#         if i % 6 == 0:
#             if i % 9 == 0:
#                 print (f'{i} je djeljiv sa 3, 6 i 9')
#                 print (f'Broj {i} nalazi se na {lista.index(i)}. poziciji.')

# i = 1
# while i < 32:
#     if i % 3 == 0 and i % 6 == 0 and i % 9 == 0:
#         print (f'{i} je djeljiv sa 3, 6 i 9')
#     i+=1
lista = []
for i in range(1, 31):
    lista.append(i)
i = 0
while i < len(lista):
    if lista[i] % 3 == 0 and lista[i] % 6 == 0 and i % 9 == 0:
        print(f'Broj {lista[i]} nalazi se na {i} poziciji.')
    i += 1

