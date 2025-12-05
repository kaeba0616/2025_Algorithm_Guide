import sys

input = sys.stdin.readline

n = int(input())
if n == 1:
    print(n)
elif n == 2:
    print(n)
else:
    i = 2
    while i * 2 < n:
        i *= 2
    print(2 * (n - i))
