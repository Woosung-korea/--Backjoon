import sys

def checkonepiece(piece):
    l = len(piece)
    std = piece[0][0]
    for i in range(l):
        for j in range(l):
            if piece[i][j] != std:
                return None
    return piece[0][0]

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
    return '(' + devide(upLeft, size // 2) + devide(upRight, size // 2) + devide(downLeft, size // 2) + devide(downRight, size // 2) + ')'

N = int(sys.stdin.readline())
paper = [0] * N
for i in range(N):
    paper[i] = sys.stdin.readline()

print(devide(paper, N))
