# 1215. [S/W 문제해결 기본] 3일차 - 회문1
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi&categoryId=AV14QpAaAAwCFAYi&categoryType=CODE&problemTitle=%5BS%2FW+%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0+%EA%B8%B0%EB%B3%B8%5D&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 22.01.08

T = 10
for t in range(T):
    N = int(input())

    pan = []
    for row in range(8):
        temp = list(input())
        pan.append(temp)

    count = 0

    # 가로 확인
    for i in range(0, 8):
        for j in range(0, 8-N+1):
            isMirror = True
            for k in range(0,int(N/2)):
                if pan[i][j+k] != pan[i][j+N-k-1]:
                    isMirror = False
                    break
            if isMirror:
                count += 1
    
    # 세로 확인
    for i in range(0, 8):
        for j in range(0, 8-N+1):
            isMirror = True
            for k in range(0,int(N/2)):
                if pan[j+k][i] != pan[j+N-k-1][i]:
                    isMirror = False
                    break
            if isMirror:
                count += 1
    
    print(f'#{t+1} {count}')

"""
range 범위 잘못 설정해서 디버깅을 했다
range 범위를 조금 더 꼼꼼히 생각하고 쓰자
"""