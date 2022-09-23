import math
print(30*'==')
print ("H adalah Ketinggian Menara")
print ("A adalah Sudut Elevasi terhadap Ujung Belakang Kapal")
print ("B adalah Sudut Elevasi terhadap Ujung Depan Kapal")
print(30*'==')
h = float(input("Silahkan Masukkan Nilai H :"))
a = float(input("Silahkan Masukkan Nilai A :"))
b = float(input("Silahkan Masukkan Nilai B :"))

x = math.tan(math.radians(a))*h
y = math.tan(math.radians(b))*h

panjang_kapal = round(math.sqrt(x-y)**2,1)

print(panjang_kapal, "m")