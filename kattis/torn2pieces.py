# https://open.kattis.com/problems/torn2pieces
# Time: 2022-09-17 14:01:35
# title: Torn To Pieces
# language: Python 3


from queue import Queue
def bfs(start_node, target_node):
    visited = set()
    queue = Queue()

    queue.put(start_node)
    visited.add(start_node)
    
    parent = dict()
    parent[start_node] = None

    path_found = False
    while not queue.empty():
        current_node = queue.get()
        if current_node == target_node:
            path_found = True
            break

        for (next_node, weight) in m_adj_list[current_node]:
            if next_node not in visited:
                queue.put(next_node)
                parent[next_node] = current_node
                visited.add(next_node)
                
    path = []
    if path_found:
        path.append(target_node)
        while parent[target_node] is not None:
            path.append(parent[target_node]) 
            target_node = parent[target_node]
        path.reverse()
    return path 
    

N = int(input())
a = {}
aa = {}
c = 0
b = []
for i in range(N):
    x = input().split()
    for j in x:
        if not j in a:
            a[j] = c
            aa[c] = j
            c += 1
    b.append(x)
m_adj_list = [[] for i in range(c)]
def add(u, v):
    u = a[u]
    v = a[v]
    m_adj_list[u].append((v, 1))
    m_adj_list[v].append((u, 1))
for i in b:
    if len(i) == 1:
        continue
    x = i[0]
    y = i[1:]
    for j in y:
        add(x, j)
u, v = input().split()
if u in a and v in a:
    p = bfs(a[u], a[v])
    if p:
        for i in p:
            print(aa[i], end=' ')
    else:
        print('no route found')
        
else:
    print('no route found')
    