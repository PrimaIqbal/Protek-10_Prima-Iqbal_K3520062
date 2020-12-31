#Nomor 7
print("------------ Program Caesar------------\n")
huruf = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
file = input("Masukkan nama file (eg = d:/anyfiles.txt) =  ")
f = open(file,"r")
data = (f.read())
n = int(input("Banyak n masukkan di Nomor 6 = "))

data = data.upper()  
result = ''

for char in data:
    if char in huruf:
        x = huruf.index(char)
        r= (x - n) % 26
        conv = huruf[r]
        result = result + conv
    else:
        result = result + ' '

data = open("c:/Users/Prima Iqbal/Documents/Nomor 6.txt", "r")
isi = data.readline()      
data.close()               

f = open("c:/Users/Prima Iqbal/Documents/Nomor 6.txt", "a+")
if result != isi:     
    f.write(result)
f.close

f = open("c:/Users/Prima Iqbal/Documents/Nomor 6.txt", "r")
baca = f.readline()
print("\n------------ OUTPUT ------------")
print("hasil ambil kode anda = ", baca)
