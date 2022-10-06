input_X = int(input("Input X : ")) #sebagai inputan nilai X
input_Y = int(input("Input Y : ")) #sebagai inputan nilai Y

if input_X < input_Y: #sebagaimana yang ada pada soal yaitu nilai X < Y
    for angka in range(1, input_Y+1): #perulangan untuk menentukan seberapa banyak angkanya (nilai Y)
        if (angka) % input_X != 0 : 
            print (angka, end = " ") #mencetak angka secara horizontal
        else:
            print(angka)
else:
    print("X harus lebih kecil dari Y") #kondisi yang dieksekusi jika X > Y