import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    ps = input().strip()
    arr = []
    is_vps = True

    for i in ps:
        if i == "(":
            arr.append(i)
        else:
            if arr:
                arr.pop()
            else:
                is_vps = False
                break

    if arr:
        is_vps = False

    if is_vps:
        print("YES")
    else:
        print("NO")
