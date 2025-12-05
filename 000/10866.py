import sys

input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    input_list = input().split()

    if input_list[0] == "push_front":
        arr.insert(0, input_list[1])
    elif input_list[0] == "push_back":
        arr.append(input_list[1])
    elif input_list[0] == "pop_front":
        print(arr.pop(0) if arr else -1)
    elif input_list[0] == "pop_back":
        print(arr.pop() if arr else -1)
    elif input_list[0] == "size":
        print(len(arr))
    elif input_list[0] == "empty":
        print(0 if arr else 1)
    elif input_list[0] == "front":
        print(arr[0] if arr else -1)
    else:
        print(arr[-1] if arr else -1)
