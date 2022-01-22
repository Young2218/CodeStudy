# 4408. 자기 방으로 돌아가기 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWNcJ2sapZMDFAV8
# 22.01.21

import math

T = int(input())
for t in range(T):
    N = int(input())

    moving = []
    for n in range(N):
        s, e = map(int, input().split())
        if s > e: s, e = e, s
        moving.append((s,e))

    max_count = [0 for _ in range(200)]
    for s,e in moving:
        for i in range(math.ceil(s/2)-1, math.ceil(e/2)):
            max_count[i] += 1

    
    print(f'#{t+1} {max(max_count)}')

"""
최적의 경우의 수를 따져야 할듯
"""