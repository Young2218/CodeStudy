# 2817. 부분 수열의 합 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7IzvG6EksDFAXB
# 22.01.24

nums = []
def find_all_case(idx, sum):
    global nums, K, N, cnt

    if idx == N:
        return
    elif sum + nums[idx] == K:
        cnt += 1
        return
    elif sum + nums[idx] > K:
        return
    
    sum += nums[idx]
    for i in range(idx+1,N):
        find_all_case(i, sum)

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    
    nums.sort()
    cnt = 0
    for i in range(0,N):
        find_all_case(i,0)

    print(f'#{t+1} {cnt}')

"""
dfs로 풀어서 시간 초과 될줄 알았는데
안되서 기분이 좋다
"""