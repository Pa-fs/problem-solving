res = 0
def go(nums, chk, n, s, sum, tmp_lst, start):
    global res
    if len(tmp_lst) > n:
        return

    if len(tmp_lst) > 0 and sum == s:
        # print(tmp_lst)
        res += 1
        # return 조심

    for i in range(start, n):
        if chk[i]:
            continue

        chk[i] = True
        tmp_lst.append(nums[i])
        go(nums, chk, n, s, sum + nums[i], tmp_lst, i + 1)
        tmp_lst.pop()
        chk[i] = False


def solution():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))

    chk = [False] * n

    go(nums, chk, n, s, 0,[], 0)
    print(res)
solution()