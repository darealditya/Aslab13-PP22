nama_file = str(input('Nama file yang ingin disalin: '))
new_file = str(input('Nama file salinan yang baru: '))

with open(nama_file, 'r') as file:
    with open(new_file, 'w') as copy:
        copy.write(file.read())

if new_file != nama_file:
    print('Berhasil')
else:
    print('Gagal')