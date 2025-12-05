import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

left = 0
right = n - 1
count = 0

while left < right:
    temp_sum = arr[left] + arr[right]

    if temp_sum == x:
        count += 1
        left += 1
        right -= 1
    elif temp_sum < x:
        left += 1
    else:
        right -= 1
print(count)
