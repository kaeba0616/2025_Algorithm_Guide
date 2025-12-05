import sys

input = sys.stdin.readline

n = int(input())

stack = []
res = []
current = 1
possible = True

for _ in range(n):
    target = int(input())

    while current <= target:
        stack.append(current)
        res.append("+")
        current += 1

    if stack[-1] == target:
        stack.pop()
        res.append("-")
    else:
        possible = False
        print("NO")
        break
if possible:
    print("\n".join(res))
