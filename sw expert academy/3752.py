# 3752 가능한 시험 점수
# 22.01.06

"""
이것도 두번째 푸는 건데 한번에 못풀고 풀었던 거 보고 풀었다 ㅠ
"""


T = int(input())
for t in range(T):
    N = int(input())
    cases = list(map(int, input().split()))

    scores = set([0])
    for c in cases:
        for s in list(scores):
            scores.add(s+c)

    print(f'#{t+1} {len(scores)}')