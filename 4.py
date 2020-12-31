f = open("c:/Users/PRIMA IQBAL/Documents/Nomor 2.txt", "r")
data = []
data2 = []
data3 = []
for line in f:
    spl = line.split("|")

pil = str(input("NIM yang mau dicari : "))
if pil in data:
    a = data.index(pil)
    print("\nData Mahasiswa:\nNIM	: ",data[a],"\nNama	: ",data2[a],"\nAlamat	: ",data3[a])
else:
    print("data tidak ditemukan mahasiswa")
