from collections import deque

n, l = map(int, input().split())
nums = [*map(int, input().split())]
dq = deque()
res = []

for i in range(n):
    if dq and dq[0] <= i - l:
        dq.popleft()
    while dq and nums[dq[-1]] >= nums[i]:
        dq.pop()
    dq.append(i)

    res.append(str(nums[dq[-1]]))

print(" ".join(res))
