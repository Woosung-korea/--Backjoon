N, M = map(int, input().split())

def get2and5(num):
    i = 1
    cnt2 = 0
    while pow(2, i) <= num:
        cnt2 += num // pow(2, i)
        i += 1
    i = 0
    cnt5 = 0
    while pow(5, i) <= num:
        cnt5 += num // pow(5, i)
        i += 1
    return [cnt2, cnt5]

first = get2and5(N)
second = get2and5(N - M)
third = get2and5(M)
ans = [first[0] - second[0] - third[0], first[1] - second[1] - third[1]]

print(min(ans))
