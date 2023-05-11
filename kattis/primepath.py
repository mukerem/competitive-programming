# https://open.kattis.com/problems/primepath
# Time: 2022-09-06 16:56:36
# title: Prime Path
# language: Python 3


a = []
def is_prime(n):
    s = int(n ** 0.5)
    for i in range(2, s+2):
        if n%i == 0:
            return False
    return True
for i in range(1000, 10000):
    if(is_prime(i)):
        a.append(i)

c = {a[i]: i for i in range(len(a))}
    
def add_edge(adj, src, dest):
    adj[src].append(dest)
    #adj[dest].append(src)

def BFS(adj, src, dest, v, pred, dist):
    queue = []
    visited = [False for i in range(v)]
  
    for i in range(v):
 
        dist[i] = 1000000
        pred[i] = -1
     
    visited[src] = True
    dist[src] = 0
    queue.append(src)
    if src == dest:
        return 1
    while (len(queue) != 0):
        u = queue[0]
        queue.pop(0)
        for i in range(len(adj[u])):
         
            if (visited[adj[u][i]] == False):
                visited[adj[u][i]] = True
                dist[adj[u][i]] = dist[u] + 1
                pred[adj[u][i]] = u
                queue.append(adj[u][i])
  
                if (adj[u][i] == dest):
                    return True
  
    return False
  
def shortest(adj, s, dest, v):

    pred=[0 for i in range(v)]
    dist=[0 for i in range(v)];
  
    q = BFS(adj, s, dest, v, pred, dist)
    if q == False:
        return -1
    return dist[dest]


v = len(a)
adj = [[] for i in range(v)]
for i in a:
    for j in a:
        if i == j:
            continue
        q = 0
        for u, vv in zip(str(i), str(j)):
            if u == vv:
                q += 1
        if q == 3:
            add_edge(adj, c[i], c[j]);

for _ in range(int(input())):
    n, m = map(int, input().split())
    
    h = shortest(adj, c[n], c[m], v)

    if h == -1:
        print('impossible')
    else:
        print(h)
