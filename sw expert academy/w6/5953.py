# 5953. 수의 새로운 비교 기준 D5
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWZ2NW8KDIEDFAUQ
# 22.02.08

def sum(num: str):
    result = 0
    for n in num:
        result += int(n)
    return result

def prod(num: str):
    result = 1
    for n in num:
        result *= int(n)+1
    return result

def intt(num: str):
    n = len(num)
    result = 0
    for i in range(1,n+1):
        result += int(num[i-1]) * 10**(n-i)
    return result

def count(start, end, ts, tp, ti) -> int:
    cnt = 0
    for i in range(start, end):
        com = str(i).zfill(N)
        com_sum = sum(com)
        if ts > com_sum: cnt += 1
        elif ts == com_sum:
            com_prod = prod(com)
            if tp > com_prod: cnt += 1
            elif tp == com_prod and ti > intt(com): cnt += 1
    
    return cnt


T = int(input())
for t in range(T):
    target = input()   
    N = len(target)

    tar_sum = sum(target)
    tar_prod = prod(target)
    tar_int = intt(target)

    result = count(0,pow(10,N),tar_sum, tar_prod, tar_int)

    print(f'#{t+1} {result+1}')
    
"""
제한시간을 통과하지 못하고 있다
"""