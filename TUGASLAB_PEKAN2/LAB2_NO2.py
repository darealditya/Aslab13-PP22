print("\n"+30*'==')
print("MENGHITUNG TOTAL TAGIHAN LISTRIK")
print(30*'==')

tarif_R1_1 = 1352
tarif_R1_2 = 1444.70
tarif_R1_3 = 1444.70
tarif_R2 = 1699.53
tarif_R3 = 1352
tarif_B2 = 1444.70
tarif_B3 = 1114.74
tarif_I3 = 1314.12
tarif_P1 = 1352

try:
    golongan = input("Silahkan Masukkan Golongan Listrik Anda : ").upper()
    daya = float(input("Silahkan Masukkan Daya Listrik Anda : "))
    pemakaian = float(input("Berapa pemakaian Listrik anda dalam sebulan : "))

    if golongan == 'R1':
        if daya == 900:
            print(f"Jumlah tagihan Anda : Rp.{tarif_R1_1 * pemakaian :,}".replace(",","/").replace("," , ".").replace("/" , ","))
        elif daya == 1300:
            print(f"Jumlah tagihan Anda : Rp.{tarif_R1_2 * pemakaian:,}".replace(",","/").replace("," , ".").replace("/" , ","))
        elif daya == 2200:
            print(f"Jumlah tagihan Anda : Rp.{tarif_R1_3 * pemakaian:,}".replace(",","/").replace("," , ".").replace("/" , ","))
        else:
            print("Input tidak Valid!")
    elif golongan == 'R2':
        if daya >= 3500 and daya <= 5500:
            print(f"Jumlah tagihan Anda : Rp.{tarif_R2 * pemakaian:,}".replace(",","/").replace("," , ".").replace("/" , ","))
        else:
            print("Input tidak Valid!")
    elif golongan == 'R3':
        if daya >= 6600 :
            print(f"Jumlah tagihan Anda : Rp.{tarif_R3 * pemakaian:,}".replace(",","/").replace("," , ".").replace("/" , ","))
        else:
            print("Input tidak Valid!")
    elif golongan == 'B2':
        if daya >= 6600 and daya <= 200000:
            print(f"Jumlah tagihan Anda : Rp.{tarif_B2 * pemakaian:,}".replace(",","/").replace("," , ".").replace("/" , ","))
        else:
            print("Input tidak Valid!")
    elif golongan == 'B3':
        if daya > 200000 :
            print(f"Jumlah tagihan Anda : Rp.{tarif_B3 * pemakaian:,}".replace(",","/").replace("," , ".").replace("/" , ","))
        else:
            print("Input tidak Valid!")
    elif golongan == 'I3':
        if daya >= 200000:
            print(f"Jumlah tagihan Anda : Rp.{tarif_I3 * pemakaian:,}".replace(",","/").replace("," , ".").replace("/" , ","))
        else:
            print("Input tidak Valid!")
    elif golongan == 'P1':
        if daya >= 6600 and daya <= 200000:
            print(f"Jumlah tagihan Anda : Rp.{tarif_P1 * pemakaian:,}".replace(",","/").replace("," , ".").replace("/" , ","))
        else:
            print("Input tidak Valid!")
except:
    print("Input tidak Valid! Inputan harus Berupa Angka!")
    
    





