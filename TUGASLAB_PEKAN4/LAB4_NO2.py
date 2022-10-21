a = int(input("masukkan bilangan 1 : "))
b = int(input("masukkan bilangan 2 : "))

def mencari_FPB (a,b):
    if a > b:
        bilangan_terbesar = a
    else:
        bilangan_terbesar = b

    for i in range(1, bilangan_terbesar+1):
        if (a % i ==0) and (b % i ==0):
            fpb = i

    return fpb

print("FPB dari" , a , "dan" , b, "=" , mencari_FPB(a,b))