# 1 1
# 2 5
# 3 9
# 4 13
n = int(input())
length = (n - 1) * 3 + n
maps = []
maps.append([' '] * length)
for _ in range(length):
    maps.append([' '] * length)
maps.append([' '] * length)

def go(r, c, n, length):
    if n == 1:
        maps[r][c] = '*'
        return
    if n == 2:
        maps[r + 2][c + 3] = '*'
        maps[r + 3][c + 2] = '*'
        maps[r + 4][c + 2] = '*'
    for i in range(length):
        maps[r][c + i] = '*' # 상
        maps[r + i + 1][c] = '*' # 좌
        maps[r + i + 2][c + length - 1] = '*' # 우
        maps[r + length + 2 - 1][c + i] = '*' # 하
        maps[r + 2][c + length - 2] = '*'

    # print(maps)
    go(r + 2, c + 2, n - 1, length - 4)


def Solution():

    go(0, 0, n, length)
    # print(maps)
    for row in maps:
        print(''.join(row).strip())
Solution()