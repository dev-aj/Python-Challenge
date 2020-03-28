data = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq
qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

output=''

for c in data:
    if ord(c) >= 97 and ord(c) <= 120:
        output = output + chr(ord(c)+2)
    elif c == 'y':
        output = output + 'a'
    elif c == 'z':
        output = output + 'b'
    else:
        output = output + c
    #print(c)

print(output)
