# Nomor 2 
while True:
    try:
        text = open("c:/Users/PRIMA IQBAL/Documents/Nomor 2.txt", "a+")
        nim = input("Masukkan NIM		: ")
        name = input("Masukkan Nama Mhs	: ")
        alamat = input("Masukkan Alamat	 \t: ")
        repeat = input("lagi(y/n)? :")
        if repeat == "n":
            text.write(nim+"|"+name+"|"+alamat+"\n")
            text.close
            text = open("c:/Users/PRIMA IQBAL/Documents/Nomor 2.txt", "r")
            print("\nisi file :")
            buka = text.read()
            print(buka)
            break
        elif repeat == "y" :
            text.write(nim+"|"+name+"|"+alamat+"\n")
            text.close
            continue
        else:
            print("inputmu salah")
            exit()
    except ValueError:
        print("input salah")
