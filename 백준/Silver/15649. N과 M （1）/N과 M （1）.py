def go(lst, n, m):
    if len(lst) == m:
        for i in lst:
            print(i, end=" ")
        print()
        return

    for i in range(1, n + 1):
        if lst.count(i):
            continue
        lst.append(i)
        go(lst, n, m)
        lst.pop()

def solution():
    n, m = map(int, input().split())

    go([], n, m)

solution()