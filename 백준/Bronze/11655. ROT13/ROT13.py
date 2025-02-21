str = input()

res = ""
for s in str:
    if s.islower():
        if ord(s) + 13 > ord('z'):
            res += chr(ord(s) - 26 + 13)
        else:
            res += chr(ord(s) + 13)
    elif s.isupper():
        if ord(s) + 13 > ord('Z'):
            res += chr(ord(s) - 26 + 13)
        else:
            res += chr(ord(s) + 13)
    else:
        res += s
print(res)