# 1238. [S/W 문제해결 기본] 10일차 - Contact D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD
# 22.01.27

t = 1
try:
    while True:
        N, start = map(int, input().split())
        input_infor = list(map(int, input().split()))
        
        graph = {}
        for i in range(0,len(input_infor), 2):
            if input_infor[i] in graph:
                graph[input_infor[i]].append(input_infor[i+1])
            else:
                graph[input_infor[i]] = [input_infor[i+1]]
        
        # max_g = start
        # visited = [0] * 101
        # visited[start] = 1
        # find_max_g(start)
        # print(f'#{t} {max_g}')

        visited = [start]
        calling = {0:[start]}
        i = 0
        while len(calling[i]) > 0:
            calling[i+1] = []
            for now in calling[i]:
                if now in graph:
                    for next in graph[now]:
                        if next not in visited:
                            calling[i+1].append(next)
                            visited.append(next)
            i+=1
        
        answer = max(calling[i-1])
        print(f'#{t} {answer}')
        t+=1

except Exception as E:
    print(E)

"""

"""