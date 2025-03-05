res = 0
def go(kit, n, k, chk, lev, w):
    global res

    if w < 500:
        return

    if lev == n:
        if w >= 500:
            res += 1
        return

    for i in range(n):
        if chk[i]:
            continue

        chk[i] = True
        go(kit, n, k, chk, lev + 1, w + kit[i] - k)
        chk[i] = False




def solution():
    n, k = map(int, input().split())
    kit = list(map(int, input().split()))

    chk = [False] * n

    go(kit, n, k, chk, 0,500)
    print(res)
solution()