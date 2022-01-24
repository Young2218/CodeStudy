# 1256. [S/W 문제해결 응용] 6일차 - K번째 접미어 D5
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV18GHd6IskCFAZN
# 22.01.24

T = int(input())
for t in range(T):
    N = int(input())
    word = input()

    wtails = []
    length = len(word)
    for i in range(0,length):
        wtails.append(word[i:length])
    
    wtails.sort()

    if len(wtails) < N:
        result = 'none'
    else:
        result = wtails[N-1]

    print(f'#{t+1} {result}')

"""
파이썬으로 풀기에는 너무 쉽다
레벨 3이나 4가 적당할듯
"""