import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [1e9]*(n+1)
heap = []

def dijkstra(start):
    dist[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for next_node, w in graph[node]:
            cost = d + w
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(heap, (cost, next_node))

start, end = map(int, input().split())
dijkstra(start)
print(dist[end])