# 5607. [Professional] 조합 D3
# 22.02.23

def fast_pow_mod(base, exp, p):
    ans = 1
    while exp > 0:
        if exp % 2:
            ans *= base
            ans %= p
            exp -= 1
        base *= base
        base %= p
        exp /= 2
    
    return ans

def give_me_answer(n, r, p) -> int:
    a = b = 1
    for i in range(1,n+1):
        a *= i
        a %= p
    
    for i in range(1,n-r+1):
        b *= i
        b %= p
    for i in range(1,r+1):
        b *= i
        b %= p
    
    b = fast_pow_mod(b,p-2,p)

    return (a*b) % p

def give_me_answer2(n, r, p) -> int:
    a = b = 1
    for i in range(n, n-r, -1):
        a *= i
        a %= p
    
    for i in range(r, 1, -1):
        b *= i
        b %= p
        
    b = fast_pow_mod(b,p-2,p)

    return (a*b) % p

T = int(input())
P = 1234567891
for t in range(1, T+1):
    N, R = map(int, input().split())
    
    print(f'#{t} {give_me_answer2(N,R,P)}')


    """
    문제에서 요구하는 것 nCr % p, (p = 1234567891)
    {n! / ((n-r)! * r!)} % p (나눗셈 연산은 모듈라 연산이 안됨)

        페르마의 소정리
        if gcd(a,p) == 1, then (a^p-1) === 1 (mod p)
        -> a*a^p-2 === 1 (mod p)
        -> a^-1 = a^p-2 (mod p)

    문제를 다시 정의
    A = n!
    B = ((n-r)! * r!) 
    -> (A * B^-1) % p
    -> (A % p) * (B^-1 % p)
    -> (A % p) * (B^p-2 % p)

        빠른 거듭제곱 구하기
    """