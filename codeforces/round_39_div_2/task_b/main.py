#   TaskB

import sys


a, b = map(int, sys.stdin.readline().split())

while True:
    if a == 0 or b == 0:
        break
    if a < b:
        if a * 2 <= b:    # step 3
            b = b - 2 * a
        elif b * 2 <= a:  # step 2
            a = a - 2 * b
        else:
            break
    elif a > b:
        if b * 2 <= a:  # step 2
            a = a - 2 * b
        elif a * 2 <= b:    # step 3
            b = b - 2 * a
        else:
            break
    else:
        break


print(a, b)
