# 1249. [S/W 문제해결 응용] 4일차 - 보급로 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD&categoryId=AV15QRX6APsCFAYD&categoryType=CODE&problemTitle=1249&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 22.01.19

T = int(input())
for t in range(T):
    N = int(input())

    road = []
    for n in range(N):
        temp = list(map(int, list(input())))
        road.append(temp)

    dp_road = [[-1 for i in range(N)] for j in range(N)]

    dp_road[0][0] = 0

    visited = set()
    while dp_road[N-1][N-1] < 0:
        local_min = -1
        for row in range(N):
            for col in range(N):
                if dp_road[row][col] >= 0 and (row,col) not in visited and (local_min < 0 or dp_road[row][col] < local_min):
                    local_min = dp_road[row][col]
                    min_idx = (row, col)
        
        r, c = min_idx
        if r > 0 and (dp_road[r-1][c] < 0 or dp_road[r-1][c] > dp_road[r][c] + road[r-1][c]):
            dp_road[r-1][c] = dp_road[r][c] + road[r-1][c]
        if r < N - 1 and (dp_road[r+1][c] < 0 or dp_road[r+1][c] > dp_road[r][c] + road[r+1][c]):
            dp_road[r+1][c] = dp_road[r][c] + road[r+1][c]
        if c > 0 and (dp_road[r][c-1] < 0 or dp_road[r][c-1] > dp_road[r][c] + road[r][c-1]):
            dp_road[r][c-1] = dp_road[r][c] + road[r][c-1]
        if c < N - 1 and (dp_road[r][c+1] < 0 or dp_road[r][c+1] > dp_road[r][c] + road[r][c+1]):
            dp_road[r][c+1] = dp_road[r][c] + road[r][c+1]
        visited.add((r,c))

    print(f'#{t+1} {dp_road[N-1][N-1]}')
