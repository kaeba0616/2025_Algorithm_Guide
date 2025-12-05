import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

res = [-1] * n
stack = []
for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        idx = stack.pop()
        res[idx] = nums[i]

    stack.append(i)

print(*res)
