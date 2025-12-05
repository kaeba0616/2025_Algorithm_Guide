import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
target_list = list(map(int, input().split()))

dq = deque(range(1, n + 1))

cnt = 0

for target in target_list:
    idx = dq.index(target)

    if idx <= len(dq) // 2:
        dq.rotate(-idx)
        cnt += idx
    else:
        move = len(dq) - idx
        dq.rotate(move)
        cnt += move

    dq.popleft()

print(cnt)
