# 1216. [S/W 문제해결 기본] 3일차 - 회문2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14Rq5aABUCFAYi&categoryId=AV14Rq5aABUCFAYi&categoryType=CODE&problemTitle=%5BS%2FW+%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0+%EA%B8%B0%EB%B3%B8%5D&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 22.01.08

def checkMirrorOdd(pan, i, j, n, isGaro) -> bool:
    if isGaro:
        if j < int(n/2) or 99 - j < int(n/2):
            return False
        for nn in range(int(n/2)):
            if pan[i][j-nn-1] != pan[i][j+nn+1]:
                return False
        return True
    else:
        if i < int(n/2) or 99 - i < int(n/2):
            return False
        for nn in range(int(n/2)):
            if pan[i-nn-1][j] != pan[i+nn+1][j]:
                return False
        return True


def checkMirrorEven(pan, i, j, n, isGaro) -> bool:
    if isGaro:
        if j < int(n/2)-1 or 99 - j <= int(n/2)-1:
            return False
        for nn in range(int(n/2)):
            if pan[i][j-nn] != pan[i][j+nn+1]:
                return False
        return True
    else:
        if i < int(n/2)-1 or 99 - i <= int(n/2)-1:
            return False
        for nn in range(int(n/2)):
            if pan[i-nn][j] != pan[i+nn+1][j]:
                return False
        return True


def findMaxOdd(pan, i, j, start, isGaro) -> int:
    n = start
    while True:
        if checkMirrorOdd(pan, i, j, n+2,isGaro):
            n += 2
        else:
            break
    return n


def findMaxEven(pan, i, j, start, isGaro) -> int:
    n = start
    while True:
        if checkMirrorEven(pan, i, j,  n+2, isGaro):
            n += 2
        else:
            break
    return n


T = 10
for t in range(T):
    input()

    pan = []
    for row in range(100):
        temp = list(input())
        pan.append(temp)

    max_m = 1

    # 가로 회문 찾기
    for i in range(100):
        for j in range(100):
            if max_m % 2 == 0:
                max_m = findMaxEven(pan, i, j, max_m, True)
                if checkMirrorOdd(pan, i, j, max_m+1, True):
                    max_m = findMaxOdd(pan, i, j, max_m+1, True)
            else:
                max_m = findMaxOdd(pan, i, j, max_m, True)
                if checkMirrorEven(pan, i, j, max_m+1, True):
                    max_m = findMaxEven(pan, i, j, max_m+1, True)
    
    # 세로 회문 찾기
    for i in range(100):
        for j in range(100):
            if max_m % 2 == 0:
                max_m = findMaxEven(pan, i, j, max_m, False)
                if checkMirrorOdd(pan, i, j, max_m+1, False):
                    max_m = findMaxOdd(pan, i, j, max_m+1, False)
            else:
                max_m = findMaxOdd(pan, i, j, max_m, False)
                if checkMirrorEven(pan, i, j, max_m+1, False):
                    max_m = findMaxEven(pan, i, j, max_m+1, False)
    
    print(f'#{t+1} {max_m}')
    
"""
생각하는 것은 어렵지 않았으나, 
생각을 코드로 구현하는 것이 오래걸림
조건문 끝에 테스트를 잘못해서 시간 추가
"""