# 1861. 정사각형 방 D4

def dfs(i: int, j: int) -> int:
    if i-1 >= 0 and rooms[i-1][j] == rooms[i][j] + 1:
        return dfs(i-1, j) + 1
    if i+1 < N and rooms[i+1][j] == rooms[i][j] + 1:
        return dfs(i+1, j) + 1
    if j-1 >= 0 and rooms[i][j-1] == rooms[i][j] + 1:
        return dfs(i, j-1) + 1
    if j+1 < N and rooms[i][j+1] == rooms[i][j] + 1:
        return dfs(i, j+1) + 1
    return 1



T = int(input())
for t in range(T):
    N = int(input())
    rooms = []
    for n in range(N):
        temp = list(map(int, input().split()))
        rooms.append(temp)

    max_move = 0
    max_room = 0
    for i in range(N):
        for j in range(N):
            result = dfs(i,j)
            if max_move < result or (result == max_move and max_room > rooms[i][j]):
                max_move = result
                max_room = rooms[i][j]

    print(f'#{t+1} {max_room} {max_move}')


"""
단순무식하게 dfs로 풀었다
"""
