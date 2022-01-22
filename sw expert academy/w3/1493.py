# 1493. 수의 새로운 연산 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b-QGqADMBBASw&categoryId=AV2b-QGqADMBBASw&categoryType=CODE&problemTitle=1493&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 22.01.21

def getCord(n) -> tuple:
    y = 1
    x = 1
    target = 1
    while True:
        if n < target: break
        target += y
        y += 1
    y -= 1
    target -= y
    
    

    while target != n:
        x += 1
        y -= 1
        target += 1
    
    return (x,y)

def getN(cord: tuple) -> int:
    x, y = cord
    
    n = 1
    for xx in range(1, x):
        n+=xx+1
    for yy in range(1,y):
        n+=yy+x-1
    
    return n


T = int(input())
for t in range(T):
    a, b = map(int, input().split())

    ax, ay = getCord(a)
    bx, by = getCord(b)

    n = getN((ax+bx, ay+by))
    print(f'#{t+1} {n}')

