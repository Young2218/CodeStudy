# 1868 지뢰찾기
# 2022.01.03



def checkBombNeighbor(map, i, j, n):
    for x in range(i-1, i+2):
        if x < 0 or x >= n: continue
        for y in range(j-1, j+2):
            if y < 0 or y >= n: continue
            elif map[x][y] != '.': continue
            map[x][y] = 'n'

def click0(map, i, j, n):
    if i < 0 or i >= n: return
    if j < 0 or j >= n: return
    if map[i][j] == 'n': 
        map[i][j] = 'p'
        return
    if map[i][j] != '.': return
    
    map[i][j] = 'p'
    for x in range(i-1, i+2):
        if x < 0 or x >= n: continue
        for y in range(j-1, j+2):
            if y < 0 or y >= n: continue
            click0(map, x, y, n)


# main ///////////////////////////////////////

T = int(input())
for t in range(0,T):
    N = int(input())
    map = []
    for n in range(0,N):
        line = list(input())
        map.append(line)
    
    count = 0

    # 지도 만들기
    for i in range(0,N):
        for j in range(0,N):
            if map[i][j] == '*': checkBombNeighbor(map, i, j, N)

    # 0 없애기
    for i in range(0,N):
        for j in range(0,N):
            if map[i][j] == '.': 
                click0(map, i, j, N)
                count += 1
    
    # n 세기
    for i in range(0,N):
        for j in range(0,N):
            if map[i][j] == 'n': 
                count += 1
    
    print(f'#{t+1} {count}')

