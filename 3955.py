import sys

T = int(sys.stdin.readline())

def getbags(people, cpb):
    n = 0
    cpp = 1
    cd = people
    candy = people * cpp + 1
    while True:
        print('cpp: ' + str(cpp))
        print('candy: ' + str(candy))
        if candy % cpb == 0:
            return (people * cpp + 1) // cpb
        else:
            if candy < cpb:
                print('Sum of candies is smaller than cpb')
                gap = (cpb - candy) // cd + 1
                cpp += gap
                candy = candy + cd * gap
                candy = candy % cpb
            else:
                print('Sum of candies is larger than cpb')
                candy = candy - (candy // cpb) * cpb
    return False

for i in range(T):
    people, cpb = map(int, sys.stdin.readline().split())
    bags = getbags(people, cpb)
    if bags == False:
        print("IMPOSSIBLE")
    else:
        print('bags: ' + str(bags))
