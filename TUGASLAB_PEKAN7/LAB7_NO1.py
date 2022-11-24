import re

s = input("Masukkan String: ")
pola = re.compile("[02468a-zA-Z]{40}[13579\s]{5}")
hasil = pola.fullmatch(s)

if pola.fullmatch(s):
    print("True")
else:
    print("False")