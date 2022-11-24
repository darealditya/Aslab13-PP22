Nama = 20
Nim = 12
Angkatan = 10

vertikal = [0, Nama+1, Nama+Nim+2, Nama+Nim+Angkatan+3]
header = ["Nama", "NIM", "Angkatan"]

file_nama = input("Masukkan nama file: ")
banyak = int(input("Berapa banyak input: "))

data = [
        {"Nama":"Aditya", "Nim":"H071221063", "Angkatan":"2022"},
        {"Nama":"Muhammad", "Nim":"H071221001", "Angkatan":"2022"}
]

with open(file_nama + ".txt", 'w') as file:
    count = 0
    mahasiswa = {
        "Nama":None,
        "Nim":None,
        "Angkatan":None
    }
    for line in file:
        if line[-1] == "\n":
            line = line[:-1]
        
        if count%3 == 0:
            mahasiswa["Nama"] = line
        elif count%3 == 1:
            mahasiswa["Nim"] = line
        elif count%3 == 2:
            mahasiswa["Angkatan"] = line
            data.append(mahasiswa.copy())
        count+=1

data_now = 0
for y in range(3 + (banyak)):
    x = 0
    while x < (Nama + Angkatan + Nim + 4):
        if y == 0 or y == 2:
            if x in vertikal:
                print("+", end="")
            else:
                print("-", end="")
        else:
            if x in vertikal:
                print("|", end="")
            else:
                if y == 1:
                    if x == 2:
                        print(header[0], end="")
                        x += (len(header[0]))
                        print(" ", end="")
                    elif x == Nama+3:
                        print(header[1], end="")
                        x += (len(header[1]))
                        print(" ", end="")
                    elif x == Nama + Nim + 4:
                        print(header[2], end="")
                        x += (len(header[2]))
                        print(" ", end="")
                    else:
                        print(" ", end="")
                else:
                    if x == 2: 
                        print(data[data_now]["Nama"], end="")
                        x += len(data[data_now]["Nama"])

                    if  x == Nama + 3: 
                        print(data[data_now]["Nim"], end="")
                        x += len(data[data_now]["Nim"])
                    
                    if  x == Nama + Nim + 4: 
                        print(data[data_now]["Angkatan"], end="")
                        x += len(data[data_now]["Angkatan"])
                    
                    print(" ", end="")
        x+=1
    if y > 2:
        data_now+=1
    print(end="\n")