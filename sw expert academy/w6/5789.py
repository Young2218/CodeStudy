# 5789. 현주의 상자 바꾸기 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWYygN36Qn8DFAVm
# 22.02.07

T = int(input())
for t in range(T):
    N, Q = map(int, input().split())

    boxs = [0]*Nz
    for q in range(1,Q+1):
        L, R = map(int, input().split())
        boxs[L-1:R] = [q]*(R-L+1)
    
    print(f'#{t+1}', end='')
    for b in boxs:
        print(f' {b}',end='')
    print()