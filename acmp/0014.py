fin = open("input.txt")
fout = open("output.txt", "w")
a, b = map(int, fin.readline().split())
an = a
bn = b
while (b > 0):
	c = a % b
	a = b
	b = c

fout.write(str((an * bn) // a))
fin.close()
fout.close()

