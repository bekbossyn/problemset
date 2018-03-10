#   118A

text = input()

vowels = ['a', 'o', 'y', 'i', 'u', 'e']

text = text.lower()
new_text = ""
for i in range(len(text)):
    if text[i] not in vowels:
        new_text += "." + text[i]
print(new_text)
