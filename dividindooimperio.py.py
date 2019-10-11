n = int(input())
adj = {}
for i in range(n - 1):
    x, y = input().split()
    if x not in adj.keys():
        adj[x] = [y]
    else:
        adj[x].append(y)
    if y not in adj.keys():
        adj[y] = [x]
    else:
        adj[y].append(x)

# A ideia seria fazer uma lista com os vértices adjacentes e procurar pelos vértices com maior quantidade de nós,
#  pois esses seriam os vértices "centrais". A partir desses vértices, fazer uma busca em profundidade para encontrar 


