l, c = map(int, input().split())
arr = list(map(str, input().split()))
vis = [False] * len(arr)
res_lst = []
tmp_lst = []
def check(string):
    aeiou = 0
    no_aeiou = 0
    for ch in string:
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch =='u':
            aeiou += 1
        else:
            no_aeiou += 1

    if aeiou >= 1 and no_aeiou >= 2:
        return True
    return False

def check_ch(string):
    for i in range(1, len(string)):
        if string[i - 1] > string[i]:
            return True

def go(lev):
    if check_ch(''.join(tmp_lst)):
        return
    if lev == l:
        if check(''.join(tmp_lst)):
            res_lst.append(''.join(tmp_lst))
        return

    for i in range(len(arr)):
        if vis[i]:
            continue
        vis[i] = True
        tmp_lst.append(arr[i])
        go(lev + 1)
        tmp_lst.pop()
        vis[i] = False
def Solution():
    go(0)
    res_lst.sort()
    for elem in res_lst:
        print(elem)

Solution()