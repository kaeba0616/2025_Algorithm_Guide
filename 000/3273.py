import sys

input = sys.stdin.readline

n = int(input())

arr = [0] * 2000002
cnt = 0

target_list = list(map(int, input().split()))

for target in target_list:
    arr[target] = 1

sum = int(input())

for target in target_list:
    if target >= sum:
        continue
    if target == (sum - target):
        continue
    if arr[target] and arr[sum - target]:
        cnt += 1

print(cnt // 2)
