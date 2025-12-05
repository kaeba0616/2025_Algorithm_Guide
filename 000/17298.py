import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
nums.reverse()

tops = [1000001]

res = []


for num in nums:
    while tops[-1] <= num:
        tops.pop()

    if tops[-1] == 1000001:
        res.append(-1)
    else:
        res.append(tops[-1])

    tops.append((num))

res.reverse()
print(*(res))
