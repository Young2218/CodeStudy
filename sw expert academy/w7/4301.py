# 4301. 콩 많이 심기 D4
# 22.02.23

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    kong = 0
    for n in range(N):
        if n % 4 < 2: x = True
        else: x = False
        for m in range(M):
            if m % 4 < 2: y = True
            else: y = False

            if not x^y: kong += 1

    print(f'#{t} {kong}')