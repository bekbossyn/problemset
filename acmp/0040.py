fin = open("input.txt")
fout = open("output.txt", "w")
n = int(fin.read())

fout.write(str(2 ** n))
fin.close()
fout.close()

