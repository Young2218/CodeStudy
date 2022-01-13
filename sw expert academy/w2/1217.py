# 1217. [S/W 문제해결 기본] 4일차 - 거듭 제곱 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14dUIaAAUCFAYD
# 22.01.12


def pow_recursive(n, p) -> int:
    if p == 1: return n
    else: return n * pow_recursive(n,p-1) 

for t in range(1,11):
    input()
    n, p = map(int, input().split())

    # 양아치 하고 싶다
    # result = pow(n,p)
    result = pow_recursive(n,p)

    print(f'#{t} {result}')