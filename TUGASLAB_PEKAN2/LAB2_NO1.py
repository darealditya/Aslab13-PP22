print("\n"+30*'==')
print("KONVERSI NILAI ANGKA KE HURUF")
print(30*'==')
nilai = int(input("Silahkan Input NILAI ANGKA : "))

if nilai >= 90:
    print(f"Nilai {nilai} = A")
elif nilai >= 80:
    print(f"Nilai {nilai} = B")
elif nilai >= 70:
    print(f"Nilai {nilai} = C")
elif nilai >= 60:
    print(f"Nilai {nilai} = D")
elif nilai >= 40:
    print(f"Nilai {nilai} = E")
elif nilai < 40:
    print(f"Nilai {nilai} = F")
else:
    print('Input tidak Valid!')