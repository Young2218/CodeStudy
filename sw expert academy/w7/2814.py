# 2814. 최장 경로 D3
# 22.02.15


def find_max_length(now_len: int, last_visit: int):
    global max_length

    if now_len > max_length:
        max_length = now_len
    for next in graph[last_visit]:
        if visited[next] == 0:
            visited[next] = 1
            find_max_length(now_len+1, next)
            visited[next] = 0


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for m in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    max_length = 1
    for i in range(1, N+1):
        visited = [0] * (N+1)
        visited[i] = 1
        find_max_length(1, i)

    print(f'#{t+1} {max_length}')
