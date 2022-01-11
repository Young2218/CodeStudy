# 1220. [S/W 문제해결 기본] 5일차 - Magnetic
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD&categoryId=AV14hwZqABsCFAYD&categoryType=CODE&problemTitle=%5BS%2FW+%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0+%EA%B8%B0%EB%B3%B8%5D&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=&pageSize=10&pageIndex=1
# 22.01.10

T = 10
for t in range(T):
    
    # 입력받기
    N = int(input())
    pan = []
    for i in range(N):
        temp = list(map(int, input().split()))
        pan.append(temp)

    count = 0
    for i in range(N):
        isN = False
        for j in range(N):
            if pan[j][i] == 0:
                continue
            elif pan[j][i] == 1:
                isN = True
                continue
            else:
                if isN:
                    count += 1
                isN = False
    
    print(f'#{t+1} {count}')

"""
메모리의 locality를 살리려다가 더 복잡해져서
컴퓨터를 조금 더 고생시키기로 했다
"""
            
    

    
    
