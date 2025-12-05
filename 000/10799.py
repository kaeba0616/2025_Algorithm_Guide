import sys

input = sys.stdin.readline

str = input().strip()

cur = 0
res = 0

for i in range(len(str)):
    if str[i] == "(":
        cur += 1
    else:
        cur -= 1
        if str[i - 1] == "(":
            res += cur
        else:
            res += 1

print(res)
