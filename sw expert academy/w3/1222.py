# 1222. [S/W 문제해결 기본] 6일차 - 계산기1 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14mbSaAEwCFAYD
# 22.01.17

for t in range(10):
    input()
    sentence = list(input())

    total_sum = 0
    for s in sentence:
        if s =='+':
            continue
        else:
            total_sum += int(s)
    

    print(f'#{t+1} {total_sum}')


"""
easy.
"""