# 13428. 숫자 조작 D3
# 22.02.23

T = int(input())
for t in range(1,T+1):
    num = list(map(int, input()))
    all_case = []
    all_case.append(int(''.join(map(str, num))))

    for i in range(1, len(num)):
        for j in range(0, i):
            if j == 0 and num[i] == 0: continue

            num[i], num[j] = num[j], num[i]
            all_case.append(int(''.join(map(str, num))))
            num[i], num[j] = num[j], num[i]

    print(f'#{t} {min(all_case)} {max(all_case)}')


    """
    복잡하게 생각하지 말고 모든 경우의 수를 구하는 방식이 더 단순할 수도 있다
    set보다 list가 좀 더 빠르다
    """