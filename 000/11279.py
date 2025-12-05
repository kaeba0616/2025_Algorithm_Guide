import heapq
import sys

input = sys.stdin.readline

n = int(input())

hq = []

for _ in range(n):
    v = int(input())
    if v == 0:
        if hq:
            print(-heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq, -v)
