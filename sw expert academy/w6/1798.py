# 1798. 범준이의 제주도 여행 계획 D5
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV4x9oyaCR8DFAUx
# 22.02.10

def find_best_route(now_day, remain_time, now_route: list, now_happy):
    global routes, information, M, visited, max_happy, happy_route, points, hotels, airport

    if remain_time < 0: return

    now = now_route[-1]
    if M == now_day:
        if remain_time < routes[now][airport]: return
        if max_happy < now_happy:
            max_happy = now_happy
            happy_route = now_route[:]
            
    else:
        for h in hotels:
            if remain_time >= routes[now][h]:
                now_route.append(h)
                find_best_route(now_day+1, 540, now_route, now_happy)
                now_route.pop(-1)

    for p in points:
        if p in visited:
            continue
        elif remain_time >= routes[now][p] + information[p][1]:
            now_route.append(p)
            visited.append(p)
            find_best_route(
                now_day, remain_time - routes[now][p] - information[p][1], now_route, now_happy+information[p][2])
            now_route.pop(-1)
            visited.pop(-1)


T = int(input())
for t in range(T):
    N, M = map(int, input().split())

    routes = [[0 for _ in range(N)] for _ in range(N)]
    for n in range(N-1):
        temp = list(map(int, input().split()))
        for i in range(0, N-n-1):
            routes[n][i+1+n] = temp[i]
            routes[i+1+n][n] = temp[i]

    information = []
    points = []
    hotels = []

    for n in range(N):
        temp = input().split()
        if temp[0] == 'P':
            information.append([temp[0], int(temp[1]), int(temp[2])])
            points.append(n)
        elif temp[0] == 'A':
            information.append(temp)
            airport = n
        else:
            information.append(temp)
            hotels.append(n)

    max_happy = 0
    happy_route = []
    visited = []
    now_route = [airport]

    find_best_route(1,540, now_route,0)

    if len(happy_route) == 0:
        print(f'#{t+1} 0')
        continue
    happy_route.pop(0)
    happy_route.append(airport)
    for i in range(len(happy_route)):
        happy_route[i] += 1

    result = ' '.join(map(str, happy_route))
    print(f'#{t+1} {max_happy} {result}')