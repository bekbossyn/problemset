#   1A

import sys

n, m, a = map(int, sys.stdin.readline().split())

result = ((n + a - 1) // a) * ((m + a - 1) // a)

print(result)
