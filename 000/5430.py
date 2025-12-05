import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    comms = input().strip()
    n = int(input())
    s = input().strip()

    if n == 0:
        dq = deque()
    else:
        dq = deque(map(int, s[1:-1].split(",")))

    reverse = False
    err = False

    for comm in comms:
        if comm == "R":
            reverse = not reverse
        else:
            if not dq:
                print("error")
                err = True
                break
            else:
                if reverse:
                    dq.pop()
                else:
                    dq.popleft()
    if not err:
        if reverse:
            dq.reverse()

        print("[" + ",".join(map(str, dq)) + "]")
