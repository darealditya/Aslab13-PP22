import os

namafile = input("Nama file yang ingin di-copy: ")
namatarget = input("Nama file hasil: ")

try:
    with open(namafile + ".txt", "r") as file:
        try:
            new = os.path.isfile(namatarget + ".txt")
            
            if new == False:
                with open(namatarget + ".txt", "w") as file1:
                    for line in file:
                        teks = "{:>60}".format(line)
                        file1.write(teks)
            else:
                for i in range(1, 255):
                    new = os.path.isfile(namatarget + str(i) + ".txt")
            
                    if new == False:
                        with open(namatarget + str(i) + ".txt", "w") as file1:
                            for line in file:
                                teks = "{:>60}".format(line)
                                file1.write(teks)
                        break
                
        except:
            print("\nGagal")
        else:
            print("\nSuccess")
except:
    print("\nGagal")