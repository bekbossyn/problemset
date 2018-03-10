#   TaskA

import sys

n = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

total = 0

for i in numbers:
    total += i if i >= 0 else -i

print(total)
