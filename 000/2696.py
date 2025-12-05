import heapq
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    hql = []
    hqr = []
    res = []

    n = int(input())
    nums = []

    while len(nums) < n:
        nums.extend(list(map(int, input().split())))

    for i in range(n):
        if len(hql) == len(hqr):
            heapq.heappush(hql, -nums[i])

        else:
            heapq.heappush(hqr, nums[i])

        if hqr and -hql[0] > hqr[0]:
            maxV = -heapq.heappop(hql)
            minV = heapq.heappop(hqr)

            heapq.heappush(hql, -minV)
            heapq.heappush(hqr, maxV)

        if i % 2 == 0:
            res.append(-hql[0])

    print(len(res))
    for i in range(0, len(res), 10):
        print(*(res[i : i + 10]))
