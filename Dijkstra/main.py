# Algorithm A *, Dijkstra

from collections import deque

# graph like a dict
graf = {"A": ["M", "P"], "B": ["P", "N"], "M": ["A", "N"], "N": ["M", "B"], "P": ["A", "B"]}

# начальную вершину помещаем в очередь и формируем словарь помещенных вершин
# в цикле пока очередь не пуста достаем первый элемент и получаем смежные вершины
# и если их нет в словаре посещенных - то помещаем их в очередь
# и записываем инфо о том с каких вершин мы пришли в текущую

def bfs(start, goal, graf):
    queue = deque([start])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = graf[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    return visited

start = 'M'
goal = 'P'
visited = bfs(start, goal, graf)

cur_node = goal
print(f"\npath from goal {goal} to {start}: \n {goal} ", end='')
while cur_node != start:
    cur_node = visited[cur_node]
    print(f"---> {cur_node}", end='')