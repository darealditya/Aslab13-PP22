import re

kondisi_ipv4 = r'(([0-1]?[\d][\d]?|2[0-4][\d]|25[0-5])\.){3}([0-1]?[\d][\d]?|2[0-4][\d]|25[0-5])$'
kondisi_ipv6 = r'(([\dA-Fa-f]{1,4}?\:){7})([\dA-Fa-f]{1,4})$'

banyak_inputan = int(input())
list = []

for inputan in range (banyak_inputan) :
    s = input()
    list.append(s)

for solving in list :
    ipv4 = re.search (kondisi_ipv4, solving)
    ipv6 = re.search (kondisi_ipv6, solving)
    if ipv4 :
        print('Ipv4')
    elif ipv6 :
        print('Ipv6')
    else :
        print('Bukan IP Address')