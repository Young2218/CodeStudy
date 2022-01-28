# 1221. [S/W 문제해결 기본] 5일차 - GNS D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14jJh6ACYCFAYD
# 22.01.27

T = int(input())
for t in range(T):
    _, N = input().split()
    N = int(N)

    nums = {'ZRO':0, 'ONE':0, 'TWO':0, 'THR':0, 'FOR':0, 'FIV':0, 'SIX':0, 'SVN':0, 'EGT':0, 'NIN':0}
    
    input_nums = list(input().split())

    for i in input_nums:
        nums[i] += 1
    
    print(f'#{t+1}', end = '')
    for k in list(nums.keys()):
        for i in range(nums[k]):
            print(' ' + str(k), end='')
    print()