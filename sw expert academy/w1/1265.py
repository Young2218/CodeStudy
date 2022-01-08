# 1265 최대상금 구하기
# 22.01.05


T = int(input())
for t in range(T):
    n, p = map(int, input().split())

    p_list = [int(n/p) for i in range(p)]
    
    d = n % p
    for i in range(p):
        if d == 0: break
        p_list[i] += 1
        d -= 1
    
    result = 1
    for i in range(p):
        result *= p_list[i]
    
    print(f'#{t+1} {result}')
