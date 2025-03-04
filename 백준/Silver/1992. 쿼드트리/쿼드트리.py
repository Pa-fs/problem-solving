res = ""
def go(maps, n):
    global res
    if n == 1:
        res += maps[0][0]
        return

    check = False
    val = maps[0][0]
    for i in range(n):
        for j in range(n):
            if val != maps[i][j]:
                check = True
    if not check:
        res += maps[0][0]
        return

    res += "("
    # 왼쪽 위 (0, 0)
    go([row[:n//2] for row in maps[:n//2]], n // 2)
    # 오른쪽 위 (0, 4)
    go([row[n//2:] for row in maps[:n//2]], n // 2)
    # 왼쪽 아래 (4, 0)
    go([row[:n//2] for row in maps[n//2:]], n // 2)
    # 오른쪽 아래 (4, 4)
    go([row[n//2:] for row in maps[n//2:]], n // 2)
    res += ")"


def solution():
    n = int(input())
    # maps = []
    # for i in range(n):
    #     maps.append(list(map(str, input().split())))
    maps = [list(input().strip()) for _ in range(n)]
    go(maps, n)

    print(res)
solution()