import re

while True:
    try:
        n = int(input('Masukkan Baris: '))
        break
    except ValueError:
        print('input angka')


ipv4_p = r'^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$'
ipv6_p = r'^(([0-9a-fA-F]{1,4}):){7}([0-9a-fA-F]{1,4}|:)|(::([0-9a-fA-F]{1,4}:){0,6}([0-9a-fA-F]{1,4}))$'

def match(ip):
    match_ipv4 = re.match (ipv4_p, ip)
    match_ipv6 = re.match (ipv6_p, ip)
    if match_ipv4:
        return('IPv4')
    elif match_ipv6:
        return('IPv6')
    else:
        return('Bukan IP Address')

lines = [input('Masukkan IP Address: ') for i in range(n)]

for line in lines:
    print(match(line))