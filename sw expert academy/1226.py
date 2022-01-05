# 1226 미로찿기
# 22.01.04

"""
왔다갔다 체크랑 처음 시작하는 2에 예외처리 잘못해서
디버깅하는데 오래걸림
작은 실수를 많이함 
"""

def isPossible(miro, i, j):
    global isFirst

    if findPath: return
    if i < 0 or i >= 16 or j < 0 or j >= 16: return False
    if miro[i][j] == 3: return True
    if miro[i][j] == 1: return False
    
    if miro[i][j] == 2: miro[i][j] -= 1
    elif miro[i][j] == 0: miro[i][j] += 1
          
    return isPossible(miro, i, j-1) or isPossible(miro, i, j+1) or isPossible(miro, i-1, j) or isPossible(miro, i+1, j)

# ////////////////////////////////////////


T = 10
for t in range(T):
    input()

    # 미로 입력 받기
    miro = []
    for i in range(16):
        temp = list(input())
        temp = list(map(int, temp))
        miro.append(temp)

    # 2를 찾고 가능한지 확인
    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                isFirst = True
                findPath = False
                if isPossible(miro, i,j):
                    print(f'#{t+1} 1')
                else:
                    print(f'#{t+1} 0')
