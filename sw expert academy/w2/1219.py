# 1219. [S/W 문제해결 기본] 4일차 - 길찾기
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14geLqABQCFAYD
# 22.01.11


visited = set()
canGo = False

def find_path(now: int):
    global path, visited, canGo, n
    
    if canGo:
        return
    elif now in visited:
        return
    elif now == 99:
        canGo = True
        return
    
    visited.add(now)
    
    for p in path[now]:
        find_path(p)

while True:  
    try:
        t, n = map(int, input().split())

        string = list(map(int, input().split()))
        path = [[] for i in range(100)]

        for i in range(0, len(string), 2):
            path[string[i]].append(string[i+1])
        
        canGo = False
        visited = set()


        find_path(0)
        if canGo:
            print(f'#{t} 1')
        else:
            print(f'#{t} 0')

    except:
        exit()

