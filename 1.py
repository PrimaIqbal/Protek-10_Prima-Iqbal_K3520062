f = open("c:/Users/Prima IQBAL/Documents/Nomor 1.txt", "r")
print(f.read())
f.close()
f = open("c:/Users/Prima IQBAL/Documents/Nomor 1.txt", "r")
jml = open("c:/Users/Prima IQBAL/Documents/jadi jumlah.txt", "a+")
data = []
data2 = []
x = 0
jml.write("\n")
for line in f:
    spl = line.split("|")
    data.append(spl[0])
    data2.append(spl[1].strip())
    x+=1
jml = open("c:/Users/Prima IQBAL/Documents/jadi jumlah.txt", "r")
baca = jml.read()
print(baca)
jml.close()
