# 1208. [S/W 문제해결 기본] 1일차 - Flatten
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh&categoryId=AV139KOaABgCFAYh&categoryType=CODE&problemTitle=%5BS%2FW+%EB%AC%B8%EC%A0%9C%ED%95%B4%EA%B2%B0+%EA%B8%B0%EB%B3%B8%5D&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 22.01.08

T = 10
for t in range(T):
    N = int(input())
    boxs = list(map(int, input().split()))

    for n in range(N):
        max_idx = boxs.index(max(boxs))
        min_idx = boxs.index(min(boxs))

        if boxs[max_idx] - boxs[min_idx] <= 1:
            break
        boxs[max_idx] -= 1
        boxs[min_idx] += 1

    max_idx = boxs.index(max(boxs))
    min_idx = boxs.index(min(boxs))
    diff = boxs[max_idx] - boxs[min_idx]
    print(f'#{t+1} {diff}')

"""
왜 2 차이가 나지? --> 실수로 for 문 끝나고 min max 안 구했다 ㅠ
"""