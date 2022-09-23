import math

PI = math.pi
print(15*'==')
diameter = float(input("Silahkan Masukkan Diameter Bola: "))
print(15*'==')
jari_jari = diameter/2
volume = (4/3) * PI * jari_jari ** 3
hasil = round(volume, 2)
print (f"MAKA VOLUME BOLA = {hasil} m kubik".format(hasil))