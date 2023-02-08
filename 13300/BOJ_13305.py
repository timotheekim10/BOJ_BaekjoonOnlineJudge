import sys
input = sys.stdin.readline

N = int(input())
distances = list(map(int, input().split()))
oil_prices = list(map(int, input().split()))

min_price = oil_prices[0]
total_price = oil_prices[0] * distances[0]
total_distance = sum(distances) - distances[0]

for i in range(1, N-1):
    if min_price > oil_prices[i]:
        min_price = oil_prices[i]

    if total_distance - distances[i] < 0:
        distance = total_distance
        total_price += min_price * distance
        break
    else:
        total_distance -= distances[i]
        distance = distances[i]
        total_price += min_price * distance

print(total_price)
