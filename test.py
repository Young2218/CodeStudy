def hanaro(N):
    check = [0xffffffffffff]*N
    check[0] = 0
    visit = [0]*N
    total_length = 0
 
    for _ in range(N):
        # 시작점 찾기
        cur = -1
        min_value = 0xffffffffffff
        for i in range(N):
            if visit[i]: continue
            if check[i] < min_value:
                cur, min_value = i, check[i]
 
        visit[cur] = 1
        total_length += min_value
 
        for j in range(N):
            if cur == j: continue
            dist_bet = (x_list[j]-x_list[cur])**2 + (y_list[j]-y_list[cur])**2
            if dist_bet < check[j]:
                check[j] = dist_bet
    return total_length
 
 
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())
 
 
    ans = round(hanaro(N) * E)
    print('#{} {}'.format(tc, ans))