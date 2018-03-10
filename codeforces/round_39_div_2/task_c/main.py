#   TaskC

text = input()

current = 0

my_alphabet = "abcdefghijklmnopqrstuvwxyz"
solved = False
begin_text = ""
end_text = ""

for i in range(len(text)):
    # new_text += text[i]
    if current > 25:
        print(begin_text + my_alphabet + end_text)
        # print(my_alphabet)
        solved = True
        break
    if ord(my_alphabet[current]) - 1 == ord(text[i]) or my_alphabet[current] == text[i]:
        if current == 0:
            begin_text = text[:i]
        if current == 25:
            try:
                end_text = text[(i + 1):]
            except:
                pass
        current += 1

if not solved:
    if current > 25:
        print(begin_text + my_alphabet + end_text)
        # print(my_alphabet)
    else:
        print(-1)
