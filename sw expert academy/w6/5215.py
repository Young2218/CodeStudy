# 5215. 햄버거 다이어트 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT
# 22.02.10


def find_best(i, now_taste, now_cal):
    global max_cal, cals, tastes, max_taste, N
    
    if now_cal >= max_cal or i >= N:
        return

    if now_cal + cals[i] <= max_cal:
        if max_taste < now_taste + tastes[i]:
            max_taste = now_taste + tastes[i]
        find_best(i+1, now_taste + tastes[i], now_cal + cals[i])
    find_best(i+1, now_taste, now_cal)



T = int(input())
for t in range(T):
    N, max_cal = map(int, input().split())
    tastes, cals = [], []
    for n in range(N):
        ta, ca = map(int, input().split())
        tastes.append(ta)
        cals.append(ca)
    max_taste = 0

    find_best(0,0,0)
    print(f'#{t+1} {max_taste}')