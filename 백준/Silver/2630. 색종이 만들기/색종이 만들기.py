white = 0
blue = 0
def dfs(maps, n):
    global white, blue

    init = 0
    diff = False
    for i in range(len(maps)):
        init = maps[0][0]
        if diff:
            break
        for j in range(len(maps[0])):
            if maps[i][j] != init:
                diff = True
                break
    if not diff:
        if init == 0:
            white += 1
        else:
            blue += 1
        return
    if n == 1:
        if maps[0][0]:
            white += 1
        else:
            blue += 1
        return

    dfs([row[:n//2] for row in maps[:n//2]], n // 2)
    dfs([row[n//2:] for row in maps[:n//2]], n // 2)
    dfs([row[:n//2] for row in maps[n//2:]], n // 2)
    dfs([row[n//2:] for row in maps[n//2:]], n // 2)


def Solution():
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]

    dfs(maps, n)
    print(white)
    print(blue)

Solution()