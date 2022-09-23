print(30*'==')
detik = int(input("MASUKKAN DETIK YANG INGIN DIKONVERSI :"))
print(30*'==')
jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print("%02d:%02d:%02d"%(jam, menit, detik))