#   71A

from pip._vendor.distlib.compat import raw_input

n = int(raw_input())
for i in range(n):
    text = raw_input()
    if len(text) > 10:
        print(text[0] + str(len(text) - 2) + text[len(text) - 1])
    else:
        print(text)
