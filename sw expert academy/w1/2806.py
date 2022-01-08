# 2806 n-queens
# 22.01.05


count = 0


def nqueens(board: list, n, i):
    global count

    if n == i:
        count += 1
        return

    for col in range(n):
        # 세로로 걸리는 것이 있나 확인
        if board.count(col) > 0:
            continue

        # 대각선으로 걸리는 있는지 확인
        cross = False
        for idx in range(0, i):
            if abs((board[idx] - col) / (idx-i)) == 1:
                cross = True
                break
        if cross:
            continue
        
        board[i] = col
        nqueens(board, n, i+1)
        board[i] = -1


T = int(input())
for t in range(T):
    n = int(input())

    board = [-1 for i in range(n)]
    count = 0

    nqueens(board,n,0)

    print(f'#{t+1} {count}')
