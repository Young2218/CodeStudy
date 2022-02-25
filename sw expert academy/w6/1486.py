# 1486. 장훈이의 높은 선반 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw
# 22.02.09

T = int(input())
for t in range(T):
    N, B = map(int, input().split())
    people = list(map(int, input().split()))
    heights = set()

    for p in people:
        for h in list(heights):
            heights.add(h+p)
        heights.add(p)

    heights = list(heights)
    heights.sort()

    for h in heights:
        if h >= B:
            print(f'#{t+1} {h-B}')
            break

"""
파이썬 집합이 이런 문제 풀기에 너무 편하다
"""