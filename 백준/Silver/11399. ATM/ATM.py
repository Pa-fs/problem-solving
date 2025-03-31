n = int(input())
prr = list(map(int, input().split()))
res = 0
def Solution():
    global res
    prr.sort()
    cur = 0
    for i in prr:
        cur += i
        res += cur
    print(res)
Solution()