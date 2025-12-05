import sys

input = sys.stdin.readline

n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]

res = []

for ns in nums:
    for v in ns:
        res.append(v)

res.sort()

print(res[-n])
