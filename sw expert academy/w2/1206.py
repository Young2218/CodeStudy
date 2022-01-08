# 1206. [S/W 문제해결 기본] 1일차 - View
# 22.01.08

T = 10
for t in range(T):
    N = int(input())
    buildings = list(map(int, input().split()))

    count = 0
    for i in range(2, N-2):
        neighbor_max = max(
            buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
        if buildings[i] > neighbor_max:
            count += buildings[i] - neighbor_max

    print(f'#{t+1} {count}')


"""
두번째 푸는 문제라 쉽게 풀었음
제한 시간이 30초라 그냥 for 문 돌렸다
while을 사용해서 조망권을 받았을 때 2씩 더하면 
조금 더 빠르게 할 수 있을 듯
"""