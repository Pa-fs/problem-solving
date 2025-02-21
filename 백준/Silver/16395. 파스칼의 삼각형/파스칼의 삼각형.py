n, k = map(int, input().split())

pascal = [[1], [1, 1]]

for i in range(2, n):
    prev = pascal.pop()
    next = [1]
    for j in range(len(prev) - 1):
        next.append(prev[j] + prev[j + 1])
    next.append(1)
    pascal.append(prev)
    pascal.append(next)

# print(pascal)
print(pascal[n - 1][k - 1])
