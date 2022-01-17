# 1247. [S/W 문제해결 응용] 3일차 - 최적 경로 D5
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15OZ4qAPICFAYD
# 22.01.17

non_visit = set()
min_distance = 0
N = 0

def get_distance(a: tuple, b: tuple) -> int:
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def find_min_distance(last_visit: tuple, total_distance):
    global points, non_visit, min_distance, N, end
    
    if min_distance > 0 and total_distance > min_distance:
        return

    if len(non_visit) == 0:
        result = total_distance + get_distance(last_visit, end)
        if min_distance < 0 or result < min_distance:
            min_distance = result
        return

    for n in list(non_visit):
        non_visit.remove(n)
        find_min_distance(points[n], total_distance+get_distance(last_visit,points[n]))
        non_visit.add(n)


T = int(input())
for t in range(T):
    N = int(input())
    xys = list(map(int, input().split()))

    start = (xys[0], xys[1])
    end = (xys[2], xys[3])
    points = []

    for n in range(4,2*N+4,2):
        points.append((xys[n], xys[n+1]))
    
    non_visit = set([i for i in range(N)])
    min_distance = -1
    
    find_min_distance(start,0)
    print(f'#{t+1} {min_distance}')


"""
두번째 푸는 문제여서 쉽게 접근했던 것 같다
"""