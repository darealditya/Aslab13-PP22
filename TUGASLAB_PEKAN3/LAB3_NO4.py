
piramid = int(input("Tinggi piramida : ")) #sebagai inputan untuk menentukan tinggi piramidnya
for i in range(1, piramid+1): #perulangan banyaknya piramid yang dicetak sesuai dari inputan
    print((piramid-i) * " " + (2*i-1) * "*") #hasil piramid yang akan dicetak