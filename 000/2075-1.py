import heapq
import sys

input = sys.stdin.readline

n = int(input())

hq = []

for i in range(n):
    nums = list(map(int, input().split()))

    if not hq:
        for num in nums:
            heapq.heappush(hq, num)
    else:
        for num in nums:
            if num > hq[0]:
                heapq.heappop(hq)
                heapq.heappush(hq, num)
print(hq[0])
