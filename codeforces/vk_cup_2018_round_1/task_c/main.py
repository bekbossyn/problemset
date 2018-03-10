#   TaskA

import sys

n = int(input())

v = list(map(int, sys.stdin.readline().split()))


my_list = list()

for i in range(n):
    ti = int(input())
    total = 0
    for j in range(i):
        if v[i] - ti <= 0:
            total += ti
            v[i] = 0
        else:
            total += ti
            v[i] -= ti
    my_list.append(total)

print(my_list, sep=" ")

for i in range(len(my_list)):
    print(my_list[i])
