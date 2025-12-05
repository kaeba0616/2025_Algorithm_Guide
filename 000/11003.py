import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())

nums = list(map(int, input().split()))

dq = deque()
res = []

for i in range(n):
    while dq and dq[-1][0] > nums[i]:
        dq.pop()

    if dq and dq[0][1] < i - l + 1:
        dq.popleft()

    dq.append((nums[i], i))
    res.append(dq[0][0])

print(*(res))
