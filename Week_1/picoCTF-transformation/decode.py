encoded = open('enc.txt', 'r',encoding='utf-8').read()
flag = ''

for ch in encoded:
    val = ord(ch)
    flag += chr(val >> 8)
    flag += chr(val & 0xFF)

print(flag)
