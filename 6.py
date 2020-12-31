#Nomor 6
f = open("c:/Users/PRIMA IQBAL/Documents/nomor 6.txt", "r")
print("------------Program Caesar------------\n")
huruf = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

data = f.read()
n = int(input("banyak n kode anda = "))
data = data.upper()   
result = ''

for char in data:
    if char in huruf:
        x = huruf.index(char)
        r = (x + n) % 26   
        conv = huruf[r]
        result = result + conv
    else:
        result = result + ' '
f.close()


print("------------ OUTPUT ------------\n")
data = open("c:/Users/Prima Iqbal/Documents/Nomor 6.txt", "r")
isi = data.readline() 
data.close
f = open("c:/Users/Prima Iqbal/Documents/Nomor 6.txt", "a+")
if result != isi:          
        f.write(result)
f.close


data = open("c:/Users/Prima Iqbal/Documents/Nomor 6.txt", "r")
baca = data.read()
print("hasil kode anda = ", baca)
data.close()
