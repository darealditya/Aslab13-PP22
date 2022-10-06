harga_barang = int(input("Harga Barang : ")) #sebagai inputan harga barang
nominal_uang = int(input("Nominal Uang : ")) #sebagai inputan nominal uang yang dibayarkan

kembalian = nominal_uang - harga_barang #rumus untuk menentukan kembalian
uang_100 = 0 #kondisi awal uang pecahan 100
uang_50 = 0 #kondisi awal uang pecahan 50
uang_20 = 0 #kondisi awal uang pecahan 20
uang_10 = 0 #kondisi awal uang pecahan 10
uang_5 = 0 #kondisi awal uang pecahan 5
uang_2 = 0 #kondisi awal uang pecahan 2
uang_1 = 0 #kondisi awal uang pecahan 1

if harga_barang < nominal_uang: #percabangan jika harga barang < nominal uangnya
    while kembalian >= 100000: #jika hasil dari rumus diatas lebih dari 100000 maka akan dilakukan perulangan untuk menghitung berapa banyak uang pecahan 100 dalam kembalian
        uang_100 += 1
        kembalian -= 100000

    while kembalian >= 50000: #logika yang sama dengan while loop pada uang 100
        uang_50 += 1
        kembalian -= 50000

    while kembalian >= 20000: #logika yang sama dengan while loop pada uang 100
        uang_20 += 1
        kembalian -= 20000

    while kembalian >= 10000: #logika yang sama dengan while loop pada uang 100 
        uang_10 += 1
        kembalian -= 10000

    while kembalian >= 5000: #logika yang sama dengan while loop pada uang 100
        uang_5 += 1
        kembalian -= 5000

    while kembalian >= 2000: #logika yang sama dengan while loop pada uang 100
        uang_2 += 1
        kembalian -= 2000

    while kembalian >= 1000: #logika yang sama dengan while loop pada uang 100
        uang_1 += 1
        kembalian -= 1000
        
    print(f"\nDetail uang kembalian anda :") #hasil yang akan dicetak sesuai pada soal tugas
    print(f"{uang_100} Uang Rp. 100.000")
    print(f"{uang_50} Uang Rp. 50.000" )
    print(f"{uang_20} Uang Rp. 20.000" )
    print(f"{uang_10} Uang Rp. 10.000" )
    print(f"{uang_5} Uang Rp. 5.000" )
    print(f"{uang_2} Uang Rp. 2.000" )
    print(f"{uang_1} Uang Rp. 1.000" )
    
else:
    print("NOMINAL UANG HARUS > HARGA BARANG!") #kondisi yang akan dicetak jika nominal uangnya < harga barangnya, karena jikalau nominal uang < harga barang itu namanya NGUTANG

