
kata= list(map(str,input("Masukkan Kata : ").strip()))
def rotasi(kata):
    for i in range(len(kata)):
        kata.insert(0, kata[-1])
        kata.pop(-1)
        print(''.join(kata), end=" | ")
rotasi(kata)
