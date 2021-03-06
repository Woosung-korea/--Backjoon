import sys

def checkcondition(rec, size):
    for i in range(len(rec) - size + 1):
        for j in range(len(rec[0]) - size + 1):
            if rec[i][j] == rec[i + size - 1][j] and rec[i][j] == rec[i][j + size - 1] and rec[i + size - 1][j] == rec[i + size - 1][j + size - 1]:
                return size
    return 0

N, M = map(int, input().split())

rec = []
for i in range(N):
    rec.append(sys.stdin.readline())
minV = 1
for j in range(2, min(N, M) + 1):
    if minV < checkcondition(rec, j):
        minV = checkcondition(rec, j)
print(minV * minV)
