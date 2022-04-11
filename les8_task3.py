# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import random


def graph_gen(vertex):
    vert = []
    graph = dict()
    for i in range(vertex):
        vert.append(i)

    for i in vert:
        vert_ch = random.choices(vert, k = random.randint(1, vertex))
        vert_ch = set(vert_ch)
        vert_ch.discard(i) # удаляет из множества саму начальную вершину, чтобы не образовывалось "петель"
        graph.update([(str(i), vert_ch)])

    return graph


n = int(input('Введите количество вершин графа: '))
g = graph_gen(n)

visited = [False] * n  # изначально ни одна из вершин не посещена
start = 0


def dfs(v):
    visited[v] = True
    for w in g[v]:
        if not visited[w]:  # посещены ли смежные вершины(берем из списка смежности)
            return dfs(w)  # рекурсия


print(g)

