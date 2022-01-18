# 2805. 농작물 수확하기 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GLXqKAWYDFAXB
# 22.01.08

T = int(input())
for t in range(T):
    N = int(input())
    hn = int(N/2)
    farm = []

    for n in range(N):
        temp = input()
        farm.append(temp)
    
    suik = ''
    for a in farm[hn]:
        suik += a

    for n in range(0,hn):
        suik += farm[n][hn-n:hn+n+1]
        suik += farm[N - n-1][hn-n:hn+n+1]
    
    money = 0
    for s in suik:
        money += int(s)

    print(f'#{t+1} {money}')
