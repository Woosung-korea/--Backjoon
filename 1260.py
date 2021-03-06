import sys


def main():
    N, M, V = map(int, sys.stdin.readline().split())
    inputList = []
    for i in range(M):
        inputList.append(sorted(list(map(int, sys.stdin.readline().split()))))
    linked = [0] * N
    for i in range(N):
        temp = []
        for j in range(M):
            if inputList[j][0] == i + 1:
                temp.append(inputList[j][1])
            elif inputList[j][1] == i + 1:
                temp.append(inputList[j][0])
        linked[i] = temp
    for i in range(N):
        linked[i] = sorted(linked[i], reverse = True)
    dfsAns = dfs(linked, V)
    printList(dfsAns)
    print()
    for i in range(N):
        linked[i] = sorted(linked[i])
    bfsAns = bfs(linked, V)
    printList(bfsAns)


def dfs(linked, V):
    ans = [] ## 방문한 node 순서대로
    stack = [V] ## stack에 저장된 node
    check = [False] * len(linked) ## 해당 노드에 방문을 했는지 확인
    while len(stack) > 0:
        sl = len(stack)
        if check[stack[sl - 1] - 1] == False: ## 방문하지 않은 노드일 때에만 ans에 추가한다.
            ans.append(stack[sl - 1]) ## stack 마지막에 있는 node에 방문
            check[stack[sl - 1] - 1] = True
        del stack[sl - 1] ## 방문한 node 삭제
        al = len(ans)
        l = len(linked[ans[al - 1] - 1]) ## 해당 노드에 연결된 node의 수
        node = ans[len(ans) - 1] ## 지금 위치한 node
        for i in range(l):
            if linked[node - 1][i] not in stack and linked[node - 1][i] not in ans:
                stack.append(linked[node - 1][i])
            elif linked[node - 1][i] in stack and linked[node - 1][i] not in ans:
                stack.append(linked[node - 1][i])
                del stack[stack.index(linked[node - 1][i])]
    return ans


def bfs(linked, V):
    ans = []
    queue = [V]
    while len(queue) > 0:
        i = 0
        while i < len(queue):
            for j in range(len(linked[queue[i] - 1])):
                if linked[queue[i] - 1][j] not in queue and linked[queue[i] - 1][j] not in ans:
                    queue.append(linked[queue[i] - 1][j])
            ans.append(queue[0])
            del queue[0]
    return ans


def printList(list):
    l = len(list)
    for i in range(l):
        print(list[i], end = ' ')


if __name__ == "__main__":
    main()
