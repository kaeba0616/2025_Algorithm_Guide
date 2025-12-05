import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

tops = [(100000001, 0)]
res = []


for i, v in enumerate(nums):
    while tops[-1][0] < v:
        tops.pop()

    res.append(tops[-1][1])

    tops.append((v, i + 1))

print(*(res))
