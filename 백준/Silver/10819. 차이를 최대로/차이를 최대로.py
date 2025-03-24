n = int(input())
arr = list(map(int, input().split()))
vis = [0] * len(arr)
res = 0
lst = []
def go(lev):
    global res
    if lev == len(arr):
        sum = 0
        for i in range(1, len(lst)):
            sum += abs(lst[i - 1] - lst[i])
        res = max(res, sum)
        return
    for i in range(len(arr)):
        if vis[i]:
            continue
        vis[i] = 1
        lst.append(arr[i])
        go(lev + 1)
        lst.pop()
        vis[i] = 0
def Solution():
    arr.sort()
    go(0)
    print(res)
Solution()