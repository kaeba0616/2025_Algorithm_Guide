import sys

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    input_list = input().split()
    if input_list[0] == "push":
        arr.append(input_list[1])
    elif input_list[0] == "pop":
        print(arr.pop() if arr else -1)
    elif input_list[0] == "size":
        print(len(arr))
    elif input_list[0] == "empty":
        print(1 if not arr else 0)
    elif input_list[0] == "top":
        print(arr[-1] if arr else -1)
