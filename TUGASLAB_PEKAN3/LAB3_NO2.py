DERAJAT_MAX = 360 #nilai konstan untuk derajat maximal yang diketahui
WAKTU_MAX_DETIK = 24 * 3600 #perhitungan untuk menentukan nilai konstan untuk waktu maximal

while True: #melakukan perulangan yang ada didalam while loop
    print(10*"==") #mencetak pembatas
    derajat = float(input("Masukkan Derajat : ")) #sebagai inputan derajat yang akan dikonversi ke waktu
    waktu_detik = (WAKTU_MAX_DETIK * derajat / DERAJAT_MAX) #rumus untuk menentukan waktu yang dikonversi dari inputan derajat
    jam = (int((waktu_detik / 3600) + 6) % 24) #waktu dalam jam
    menit = int((waktu_detik % 3600) / 60)#waktu dalam menit
    detik = int(waktu_detik % 60)#waktu dalam detik
    if derajat >= 0 and derajat <= 360: #percabangan jika nilai inputan derajat itu 0 - 360
        if jam >= 1 and jam <= 5: #percabangan jika waktu dalam jam menunjukkan pukul 1 - 5
            print(f"Masih Dini Hari, Jangan lupa Sholat Subuh!\n{jam}:{menit}:{int(detik)}") #hasil yang dicetak jika jam menunjukkan pukul 1 - 5
        elif jam >= 6 and jam < 12: #logika yang sama dengan yang diatas
            print(f"Selamat Pagi\n{jam}:{menit}:{int(detik)}")
        elif jam >= 12 and jam < 15: #logika yang sama dengan yang diatas
            print(f"Selamat Siang\n{jam}:{menit}:{int(detik)}")
        elif jam >= 15 and jam < 18: #logika yang sama dengan yang diatas
            print(f"Selamat Sore\n{jam}:{menit}:{int(detik)}")
        elif jam >= 18: #logika yang sama dengan yang diatas
            print(f"Selamat Malam\n{jam}:{menit}:{int(detik)}")
    else:
        print("Nilai inputan hanya 0 - 360") #kondisi yang dicetak jika inputan derajat melebihi 360
        break  #untuk menghentikan kondisi perulangan
      
