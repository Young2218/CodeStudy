# 1209. [S/W 문제해결 기본] 2일차 - Sum
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=1209&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 22.01.11

T = 10
for t in range(T):
    input()

    pan = []
    for i in range(100):
        temp = list(map(int, input().split()))
        pan.append(temp)

    max = 0

    # 가로 찾기
    for p in pan:
        s = sum(p)
        if max < s:
            max = s
    
    # 세로 찾기
    for i in range(100):
        s = 0
        for j in range(100):
            s += pan[j][i]
        
        if max < s:
            max = s
    
    # 대각선 찾기
    s = 0
    s1 = 0
    for i in range(100):
        s += pan[i][i]
        s1 += pan[i][99-i]
    if max < s:
        max = s
    if max < s1:
        max = s1

    print(f'#{t+1} {max}')

"""
배열 순서를 눈을 잘뜨고 넣자
"""