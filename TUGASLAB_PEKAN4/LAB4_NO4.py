
angka = int(input("Masukkan Angka : "))
def faktorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return (number * faktorial(number - 1))

print(f"Nilai Faktorial dari {angka} adalah {faktorial(angka)}")
