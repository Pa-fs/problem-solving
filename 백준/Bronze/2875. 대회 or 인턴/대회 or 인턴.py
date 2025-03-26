import math

n, m, k = map(int, input().split())
def Solution():
    global n, m, k
    t = 0
    while n - 2 >= 0 and m - 1 >= 0:

        n = n - 2
        m = m - 1
        t += 1

    if n + m >= k:
        print(t)
    else:
        k = k - (n + m)
        t = t - math.ceil(k / 3)
        print(t)

Solution()