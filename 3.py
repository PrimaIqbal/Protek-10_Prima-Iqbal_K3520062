#Nomor 3
text = open("c:/Users/PRIMA IQBAL/Documents/Nomor 3.txt", "r")
line = text.readlines()
text = len(line)
for tex in range(0,text):
        a = line[x]
        spl = a.split("|")
        a = spl[0]
        y = spl[1]
        z = spl[2].replace("\n", "")
        x+=1
        lis = {"nim":a,"name":y,"alamat":z}
print(g1)
