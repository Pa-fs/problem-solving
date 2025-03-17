n = int(input())
def Solution():
    res = 0
    for _ in range(n):
        s = input()
        stack = []

        for ch in s:
            if len(stack) > 0 and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        if len(stack) == 0:
            res += 1
    print(res)
Solution()