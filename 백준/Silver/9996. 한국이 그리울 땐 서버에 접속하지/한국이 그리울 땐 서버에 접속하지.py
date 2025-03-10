n = int(input())
std = input()
star = std.find('*')
pfx = std[:star]
sfx = std[star + 1:]
def Solution():
    for _ in range(n):
        s = input()

        if len(s) < len(pfx) + len(sfx):
            print("NE")
            continue

        if pfx == s[0:len(pfx)] and sfx == s[len(s) - len(sfx):]:
            print("DA")
        else:
            print("NE")
Solution()