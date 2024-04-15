import sys
import heapq

input = sys.stdin.readline

INF = 1e9

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [INF]*(V+1)

q = []

def dijkstra(start):
    dist[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        d, node = heapq.heappop(q)
        for next_node, w in graph[node]:
            cost = d + w
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(q, (cost, next_node))

dijkstra(start)

for i in dist[1:]:
    if i != INF:
        print(i)
    else:
        print('INF')