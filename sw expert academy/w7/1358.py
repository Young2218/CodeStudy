# 1258. [S/W 문제해결 응용] 7일차 - 행렬찾기 D4

T = int(input())
for t in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for n in range(N)]

    result = []
    row = 0
    while row < N:
        if sum(mat[row]) == 0:
            row += 1
            continue

        # left-top 찾기
        for n in range(N):
            if mat[row][n] != 0:
                lt = (row, n)
                break
        
        # 열 갯수 찾기
        n = lt[1]
        while n < N:
            if mat[row][n] == 0: break
            n += 1
        i = n - lt[1]

        # 행 갯수 찾기
        n = row
        while n < N:
            if mat[n][lt[1]] == 0: break
            n += 1
        j = n - row

        result.append((i*j, j, i))

        # 찾은 친구 지우기
        for ii in range(row, row + j):
            for jj in range(lt[1], lt[1]+i):
                mat[ii][jj] = 0

    result.sort(key= lambda x:(x[0], x[1]))

    rc = []
    for r in result:
        rc.append(r[1])
        rc.append(r[2])
    rc_str = ' '.join(map(str, rc))
    print(f'#{t} {len(result)} {rc_str}')

"""
람다를 사용해서 소팅을 해보았다
"""