import sys

input = sys.stdin.readline

n, m = list(map(int, input().strip().split()))

arr = [i + 1 for i in range(int(n))]

cur = 0
cnt = 0

target_list = list(map(int, input().strip().split()))

for tar in target_list:
    i = arr.index(tar)
    diff = abs(cur - i)
    cnt += min(diff, len(arr) - diff)
    arr.remove(tar)
    cur = i
    if i >= len(arr):
        i = 0
print(cnt)
