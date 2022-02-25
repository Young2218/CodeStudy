# 1245. [S/W 문제해결 응용] 2일차 - 균형점 D5


T = int(input())
for t in range(1, T+1):
    N = int(input())
    temp = list(map(int, input().split()))

    X = temp[:N]
    M = temp[N:]
    answer = []

    for i in range(1,N):
        left = X[i-1]
        right = X[i]
        
        while right - left > 1 /10**12:
            mid = (right + left) / 2

            left_side = right_side = 0
            for n in range(N):
                force = M[n]/(mid - X[n])**2
                
                if X[n] > mid:
                    right_side += force
                else:
                    left_side += force
            
            if right_side > left_side:
                right = mid
            else:
                left = mid

        answer.append(mid)
    
    answer_str = ' '.join('%.10f' % f for f in answer)
    print(f'#{t} {answer_str}')

    

"""
처음에 문제를 잘못 이해하고 잘 못 풀었다
(이차방적식의 근의 공식을 이용해서 풀었다)
"""

"""
정답을 보고 다시 풀었다
오차가 매우 작은 정답을 풀 때 이런 형식으로 풀면 좋을 것 같다
"""

"""
나누기 연산이 꽤 시간을 많이 잡아 먹는다
0.1 의 12제곱보다 1나누기 10의 12제곱이 시간이 짧다
"""