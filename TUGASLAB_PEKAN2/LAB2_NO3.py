print("\n"+30*'==')
print("MENENTUKAN NILAI TERBESAR DARI TIGA ANGKA")
print(30*'==')

a = int(input("Masukkan Nilai A : "))
b = int(input("Masukkan Nilai B : "))
c = int(input("Masukkan Nilai C : "))
print(30*'==')

if a > b and a > c:
    print(f"{a} atau Nilai A adalah Nilai terbesar")
elif b > a and b > c:
    print(f"{b} atau Nilai B adalah Nilai terbesar")
elif c > a and c > b:
    print(f"{c} atau Nilai C adalah Nilai terbesar")
else:
    print("Nilai dari Tiga angka tersebut adalah sama.")
