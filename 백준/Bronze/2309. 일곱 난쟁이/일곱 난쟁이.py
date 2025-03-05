check = [False] * 9
sum = 0
found_sum = False
found_lst = []
def go(lst, lev, tmp):
    global sum, found_sum, found_lst

    if found_sum:
        return
    if lev == 7:
        for elem in tmp:
            sum += elem
        if sum == 100:
            found_sum = True
            found_lst = tmp[:]
        else:
            sum = 0
        return

    for i in range(len(lst)):
        if check[i]:
            continue

        check[i] = True
        tmp.append(lst[i])
        go(lst, lev + 1, tmp)
        tmp.pop()
        check[i] = False

def solution():
    lst = []
    for _ in range(9):
        lst.append(int(input()))

    go(lst, 0, [])

    found_lst.sort()
    for elem in found_lst:
        print(elem)

solution()