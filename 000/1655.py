import heapq
import sys

input = sys.stdin.readline

hql = []
hqr = []
res = []

n = int(input())

for i in range(n):
    num = int(input())

    if len(hql) == len(hqr):
        heapq.heappush(hql, -num)
    else:
        heapq.heappush(hqr, num)

    if hqr and -hql[0] > hqr[0]:
        maxV = -heapq.heappop(hql)
        minV = heapq.heappop(hqr)

        heapq.heappush(hql, -minV)
        heapq.heappush(hqr, maxV)

    res.append(hql[0])

for i in range(n):
    res[i] = -res[i]

print(*(res))
