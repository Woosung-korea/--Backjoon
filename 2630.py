import sys

def checkonepiece(piece):
    l = len(piece)
    std = piece[0][0]
    for i in range(l):
        for j in range(l):
            if piece[i][j] != std:
                return None
    if std == '0':
        return [1, 0]
    else:
        return [0, 1]

def devide(paper, size):
    chk = checkonepiece(paper)
    if chk != None:
        return chk
    upLeft = [0] * (size // 2)
    upRight = [0] * (size // 2)
    for i in range(size // 2):
        upLeft[i] = paper[i][:size // 2]
        upRight[i] = paper[i][size // 2:]
    downLeft = [0] * (size // 2)
    downRight = [0] * (size // 2)
    for i in range(size // 2, size):
        downLeft[i - size // 2] = paper[i][:size // 2]
        downRight[i - size // 2] = paper[i][size // 2:]
    a = devide(upLeft, size // 2)
    b = devide(upRight, size // 2)
    c = devide(downLeft, size // 2)
    d = devide(downRight, size // 2)
    return [a[0] + b[0] + c[0] + d[0], a[1] + b[1] + c[1] + d[1]]

N = int(sys.stdin.readline())
paper = [0] * N
for i in range(N):
    paper[i] = sys.stdin.readline()[:2 * N - 1]

for i in range(N):
    temp = ''
    for j in range(N):
        temp += paper[i][2 * j]
    paper[i] = temp

ans = devide(paper, N)
print(ans[0])
print(ans[1])
