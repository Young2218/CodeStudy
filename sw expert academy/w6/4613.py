# 4613. 러시아 국기 같은 깃발 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWQl9TIK8qoDFAXj
# 22.02.07

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    cflag = []
    for n in range(N):
        cflag.append(input())
    
    min = N*M
    for blue_start in range(1,N-1):
        for blue_end in range(blue_start,N-1):
            cnt = 0
            # white
            for w in range(0,blue_start):
                cnt += M - cflag[w].count('W')
            # blue
            for b in range(blue_start,blue_end+1):
                cnt += M - cflag[b].count('B')
            # red
            for r in range(blue_end+1,N):
                cnt += M - cflag[r].count('R')
            
            if cnt < min:
                min = cnt
    
    print(f'#{t+1} {min}')
