#   158A

import sys

n, k = map(int, sys.stdin.readline().split())

accepted_cnt = 0
num_list = list(map(int, sys.stdin.readline().split()))
last = 0
for pk in range(0, k):
    if num_list[pk] < 1:
        break
    accepted_cnt += 1

pk = k

while num_list[k - 1] > 0 and pk < len(num_list):
    if num_list[k - 1] == num_list[pk]:
        accepted_cnt += 1
    else:
        break
    pk += 1
print(accepted_cnt)
