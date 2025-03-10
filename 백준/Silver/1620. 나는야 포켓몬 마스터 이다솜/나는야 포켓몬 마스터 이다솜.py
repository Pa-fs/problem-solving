dic1 = {}
dic2 = {}
def Solution():
    n, m = map(int, input().split())
    for i in range(n):
        val = input()
        dic1[i + 1] = val
        dic2[val] = i + 1

    # print(dic1)
    # print(dic2)
    for _ in range(m):
        val = input()

        if val.isalpha():
            print(dic2[val])
        else:

            print(dic1[int(val)])
Solution()