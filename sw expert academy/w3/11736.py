# 11736. 평범한 숫자 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXhh-H-KwUcDFARQ
# 22.01.08

T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    count = 0
    for n in range(1,N-1):
        if nums[n] != min(nums[n-1], nums[n], nums[n+1]) and nums[n] != max(nums[n-1], nums[n], nums[n+1]):
            count += 1
    
    print(f'#{t+1} {count}')