n = int(input())

nums = [1,2,3]
sum_lst = []
res = 0
def go(target, sum, start):
    global res
    if target < sum:
        return
    if target == sum:
        res += 1
        return

    for i in range(len(nums)):
        sum_lst.append(nums[i])
        go(target, sum + nums[i], 0)
        sum_lst.pop()

def Solution():
    global res, sum_lst
    for _ in range(n):
        res = 0
        sum_lst.clear()
        num = int(input())

        go(num, 0, 0)
        print(res)

Solution()