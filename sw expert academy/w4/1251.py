# 1251. [S/W 문제해결 응용] 4일차 - 하나로 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15StKqAQkCFAYD
# 22.01.26

def get_length(xs, ys, a: int, b: int) -> float:
    return (xs[a]-xs[b])**2 + (ys[a]-ys[b])**2

def get_mst_prim(all_length, N) -> float:
    visited = [0]*N
    visited[0] = 1
    result = 0

    for _ in range(N-1):
        local_min, min_idx = -1, -1
        for i in range(N):
            if visited[i] == 0: continue
            for j in range(N):
                if visited[j] == 1: continue
                if local_min < 0 or local_min > all_length[i][j]:
                    local_min = all_length[i][j]
                    min_idx = j

        visited[min_idx] = 1
        result += local_min

    return result


def get_mst_kruskal():
    pass


T = int(input())
for t in range(T):
    # input
    N = int(input())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    E = float(input())

    # calculate all length
    all_length = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            length = get_length(xs, ys, i, j)
            all_length[i][j] = length
            all_length[j][i] = length

    # find cheapest way: prim
    result = get_mst_prim(all_length, N)

    print(f'#{t+1} {int(round(result*E,0))}')
