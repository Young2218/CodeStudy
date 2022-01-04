# 1210 ladder1
# 22.01.04

def findStartPoint(ladder, i, j) -> int:
    if i == 0: return j

    ladder[i][j] = 5
    if j-1 > 0 and ladder[i][j-1] == 1: return findStartPoint(ladder, i, j-1)
    elif j+1 < 100 and ladder[i][j+1] == 1: return findStartPoint(ladder, i, j+1)
    else: return findStartPoint(ladder, i-1, j)

T = 10
for t in range(T):
    input()

    # 사다리 입력 받기
    ladder = []
    for i in range(100):
        temp = list(map(int, input().split()))
        ladder.append(temp)

    # find 2
    for i in range(100):
        if ladder[99][i] == 2:
            result = findStartPoint(ladder, 99, i)
            print(f'#{t+1} {result}')
            break
