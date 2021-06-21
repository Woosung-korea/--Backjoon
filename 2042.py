import sys


def main():
    N, M, K = map(int, sys.stdin.readline().split())
    i = 0
    while 1:
        if pow(2, i) >= N:
            tree = [0] * pow(2, i + 1)
            coverIdx = [[-1, -1] for j in range(pow(2, i + 1))]
            sIdx = pow(2, i) - 1
            break
        i += 1
    for i in range(1, N + 1):
        val = int(sys.stdin.readline())
        tree[sIdx + i] = val
    for i in range(sIdx + 1, len(coverIdx)):
        coverIdx[i] = [i, i]
    for idx in range(len(tree) - 1, 1, -1):
        tree[idx // 2] += tree[idx]
        if idx % 2 == 1:
            coverIdx[idx // 2][1] = coverIdx[idx][1]
        else:
            coverIdx[idx // 2][0] = coverIdx[idx][0]
    for i in range(K):
        a, b, c = map(int, sys.stdin.readline().split())
        if a == 1:
            changeNum(sIdx + b, c - tree[sIdx + b], tree)
        else:
            print(getSum(b, c, tree, coverIdx))


def changeNum(idx, diff, tree):
    while idx >= 1:
        tree[idx] += diff
        idx = idx // 2


def getSum(start, end, tree, coverIdx):

    return 0


if __name__ == '__main__':
    main()
