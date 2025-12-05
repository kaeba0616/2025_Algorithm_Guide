import heapq
import sys

input = sys.stdin.readline

n = int(input())

hq = []
res = 0

for _ in range(n):
    heapq.heappush(hq, int(input()))

while len(hq) > 1:
    num1 = heapq.heappop(hq)
    num2 = heapq.heappop(hq)

    sum = num1 + num2
    res += sum

    heapq.heappush(hq, sum)

print(res)
