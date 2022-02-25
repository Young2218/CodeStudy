# 1860. 진기의 최고급 붕어빵 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LsaaqDzYDFAXc
# 22.02.09

T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    orders = list(map(int, input().split()))

    orders.sort()
    bbang = 0
    now = 0
    while len(orders):
        if now != 0 and now % M == 0:
            bbang += K

        if now >= orders[0]:
            if bbang > 0:
                orders.pop(0)
                bbang -= 1
            else:
                break
        
        now += 1

    if len(orders):
        print(f'#{t+1} Impossible')
    else:
        print(f'#{t+1} Possible')


"""
생각보다 시간이 오래걸림
"""