# 3499. 퍼펙트 셔플 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWGsRbk6AQIDFAVW
# 22.02.07

import math

T = int(input())
for t in range(T):
    N = int(input())
    cards = input().split()

    deck_a = cards[0:math.ceil(N/2)]
    deck_b = cards[math.ceil(N/2):N]

    print(f'#{t+1}',end='')
    for i in range(0,int(N/2)):
        print(f' {deck_a[i]} {deck_b[i]}',end='')
    
    if N%2 == 0:
        print()
    else:
        print(f' {deck_a[-1]}')
