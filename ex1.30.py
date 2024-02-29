conjunto1 = set(map(int, input('Digite os elementos do primeiro conjunto (Separando por espaço): ').split()))

conjunto2 = set(map(int, input('Digite os elementos do segundo conjunto (Separando por espaço): ').split()))

uniao = conjunto1.union(conjunto2)
print(f'União: {uniao}')

intersecao = conjunto1.intersection(conjunto2)
print(f'Interseção: {intersecao}')

diferenca1 = conjunto1.difference(conjunto2)
print(f'Diferença (conjunto1 - conjunto2): {diferenca1}')

diferenca2 = conjunto2.difference(conjunto1)
print(f'Diferença (conjunto2 - conjunto1): {diferenca2}')
