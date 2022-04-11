# 1. На улице встретились N друзей.
# Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?

n = int(input('Введите количество друзей: '))

graph = [[int(i > j) for i in range(n)] for j in range(n)]
print(graph)
handshakes = 0
for i in graph:
    for q in i:
        handshakes += q
print(f'Число рукопожатий между {n} друзьями равно {handshakes}')