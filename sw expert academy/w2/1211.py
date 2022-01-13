# 1211. [S/W 문제해결 기본] 2일차 - Ladder2 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14BgD6AEECFAYh
# 22.01.12

def get_distance_travel(ladder, start) -> int:
    distacne = 0
    j = start
    for i in range(100):
        if  j > 0 and ladder[i][j-1] == 1:
            while j > 0 and ladder[i][j-1] == 1:
                distacne += 1
                j -= 1
            continue
        elif j < 99 and ladder[i][j+1] == 1:
            while j < 99 and ladder[i][j+1] == 1:
                distacne += 1
                j += 1
            continue
    
    return distacne

for t in range(1,11):
    # 입력받기
    input()
    ladder = []
    for i in range(100):
        temp = list(map(int, input().split()))
        ladder.append(temp)

    # 가장 짧은 이동 거리를 찾기
    min_idx = -1
    min_distance = -1
    for i in range(100):
        if ladder[0][i] == 1:
            temp = get_distance_travel(ladder, i)
            if min_distance < 0 or temp < min_distance:
                min_distance = temp
                min_idx = i
    
    print(f'#{t} {min_idx}')
    