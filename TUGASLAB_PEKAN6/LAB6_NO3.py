from prettytable import PrettyTable

table = PrettyTable(['Nama', 'NIM', 'Angkatan'])
table.add_row([])
nama_file = input('Nama file: ')
banyak_data = int(input('Jumlah Asisten: '))
jumlah_asisten = banyak_data * 3
# isi_data = str(input(''))
for i in range (0, jumlah_asisten):
    isi_data = input("- ")
    isi_data1 = ''.join(table)
    
with open(nama_file, 'w') as file:
    file.write(table)
inputan1 = list(map(str,input('').split(' ')))
table.add_row(inputan1[0])
print(table)