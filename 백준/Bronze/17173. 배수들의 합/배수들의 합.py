n, m = map(int, input().split())
lst = list(map(int, input().split()))
def Solution():
    res = 0

    for i in range(1, n + 1, 1):
        bool = False
        for j in range(len(lst)):
            if i % lst[j] == 0:
                bool = True
        if bool:
            res += i
    print(res)
Solution()