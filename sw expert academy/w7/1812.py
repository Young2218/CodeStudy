# 1812. 수정이의 타일 자르기 D5

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    max_S = max(S)
    tiles = [0] * (max_S+1)
    mtiles = [0] * (max_S+1)
    for s in S:
        tiles[s] += 1

    de = M
    while de >= 1:
        for i in range(max_S, -1, -1):
            pow_i = pow(2,i)
            if de >= pow_i:
                mtiles[i] += (de // pow_i)**2
                mtiles[i] += 2 * ((M-de)// pow_i)
                de -= pow_i

    answer = 1
    answer_tiles = mtiles[:]
    for i in range(max_S, -1, -1):
        while answer_tiles[i] < tiles[i]:
            answer += 1
            answer_tiles = [a+b for a,b in zip(answer_tiles, mtiles)]
            for j in range(max_S-1, i-1, -1):
                answer_tiles[j] += answer_tiles[j+1]*4
                answer_tiles[j+1] = 0
        answer_tiles[i] -= tiles[i]
        if i > 0:
            answer_tiles[i-1] += answer_tiles[i]*4
            answer_tiles[i] = 0

    print(f'#{t} {answer}')

"""
중간에 무한루프 나와서 시간초과 나오고
논리 오류가 몇개 있어서 디버깅을 좀 했다
디버깅을 좀 해보고 생각하자
"""