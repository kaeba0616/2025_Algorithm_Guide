import sys

input = sys.stdin.readline

s = input().strip()

mux = 1
sum = 0

stack = []
for i in range(len(s)):
    c = s[i]
    if c == "(":
        mux *= 2
        stack.append(c)
    elif c == "[":
        mux *= 3
        stack.append(c)
    elif c == ")":
        if not stack or stack[-1] != "(":
            sum = 0
            break
        if s[i - 1] == "(":
            sum += mux
        stack.pop()
        mux //= 2

    else:
        if not stack or stack[-1] != "[":
            sum = 0
            break
        if s[i - 1] == "[":
            sum += mux
        stack.pop()
        mux //= 3
if stack:
    print(0)
else:
    print(sum)
