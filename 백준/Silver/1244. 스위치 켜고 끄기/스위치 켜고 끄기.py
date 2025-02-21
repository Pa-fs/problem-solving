N = int(input())
switch = list(map(int, input().split()))
switch.insert(0, 0)

std_cnt = int(input())


def male(switch, number):
    for i in range(1, len(switch)):
        if i % number == 0:
            switch[i] = (switch[i] + 1) % 2

def femail(switch, number):
    x, y = number, number
    switch[x] = (switch[x] + 1) % 2

    while x - 1 >= 1 and y + 1 < len(switch):
        nx, ny = x - 1, y + 1
        if switch[nx] == switch[ny]:
            switch[nx] = (switch[nx] + 1) % 2
            switch[ny] = (switch[ny] + 1) % 2
        else:
            return
        x, y = nx, ny

for _ in range(std_cnt):
    gender, number = map(int, input().split())
    if gender == 1:
        male(switch, number)
    else:
        femail(switch, number)

for i in range(1, len(switch)):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()