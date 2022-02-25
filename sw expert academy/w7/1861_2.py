# 1861. 정사각형 방 D4


T = int(input())
for t in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*(N*N+1)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(N):
        for j in range(N):
            for dd in range(4):
                x = j + dx[dd]
                y = i + dy[dd]

                if 0 <= x < N and 0 <= y < N:
                    if rooms[y][x] == rooms[i][j] + 1:
                        visited[rooms[i][j]] = 1
    
    cnt = 1
    max_cnt = 1
    max_room = N*N
    for i in range(N*N, 0, -1):
        if not visited[i]:
            if cnt >= max_cnt:
                max_cnt = cnt
                max_room = i + 1
            cnt = 1
        else:
            cnt += 1
            
    if cnt >= max_cnt:
        max_cnt = cnt
        max_room = 1
    
    print(f'#{t} {max_room} {max_cnt}')

"""
1,2등 것을 보고 다시 풀어봤다
새로운 방식을 배웠다
"""