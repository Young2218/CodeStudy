# 13038. 교환학생 D3

T = int(input())
for t in range(1, T+1):
    n = int(input())
    week = list(map(int, input().split()))

    s = sum(week)
    days = 0
    while n > s:
        n -= s
        days += 7

    min = 7
    for d in range(7):
        remain = n
        temp = 0
        while remain > 0:
            temp += 1
            if week[(d+temp)%7]:
                remain-=1
        if min > temp:
            min = temp
    
    print(f'#{t} {days+min}')
        
"""
조금 무식하게 while로 빼줬는데
규칙을 더 정확하게 찾으면 시간 단축 가능할듯
근데 코드는 길어질 듯하다
"""