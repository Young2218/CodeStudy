# 1244 최대상금구하기
# 22.01.06

"""
이거 두번째 푸는데 왜케 안풀리냐...
"""
max = -1
visited = set()


def digit2int(digits) -> int:
    result = 0
    for d in digits:
        result = result*10 + d
    return result   

def check_all_case(n):
    global digits, max, visited

    if n <= 0:
        result = digit2int(digits)
        if result > max:
            max = result
        return
    else:
        for i in range(len(digits)):
            for j in range(i+1,len(digits)):
                digits[i], digits[j] = digits[j], digits[i]

                if not (digit2int(digits), n-1) in visited:
                    check_all_case(n-1)
                    visited.add((digit2int(digits), n-1))

                digits[i], digits[j] = digits[j], digits[i]
        

T = int(input())
for t in range(T):
    digits, N = input().split()

    digits = list(map(int, list(digits)))
    N = int(N)
    max = -1
    visited = set()
    check_all_case(N)
    
    print(f'#{t+1} {max}')