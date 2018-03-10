#   TaskA

import sys

n = int(input())

v = list(map(int, sys.stdin.readline().split()))
list_ti = list(map(int, sys.stdin.readline().split()))


my_list = list()

for i in range(n):
    ti = list_ti[i]
    total = 0
    for j in range(i + 1):
        if v[j] - ti <= 0:
            total += v[j]
            v[j] = 0
        else:
            total += ti
            v[j] -= ti
    my_list.append(total)

print(' '.join(str(my_list[x]) for x in range(len(my_list))))
