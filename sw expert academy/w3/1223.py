# 1223. [S/W 문제해결 기본] 6일차 - 계산기2 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14nnAaAFACFAYD
# 22.01.17


for t in range(10):
    n = int(input())
    sentence = list(input())

    giho = []
    postfix = []

    # postfix 방식으로 표현하기
    for s in sentence:
        if s == '*' or s == '+':
            if len(giho) == 0:
                giho.append(s)
            else:
                last_giho = giho.pop()
                if last_giho <= s: # '+' > '*'
                    postfix.append(last_giho)
                    giho.append(s)
                else:
                    giho.append(last_giho)
                    giho.append(s)
        else:
            postfix.append(int(s))
    
    giho.reverse()
    for g in giho:
        postfix.append(g)

    nums = []
    # calculate
    for p in postfix:
        if p == '*' or p == '+':
            n1 = nums.pop()
            n2 = nums.pop()

            if p == '*':
                nums.append(n1*n2)
            else:
                nums.append(n1+n2)
        else:
            nums.append(p)

    print(f'#{t+1} {nums.pop()}')


    
"""
postfix 를 잘 몰라서 검색해서 풀었다
나중에 다시한번 풀어봐야 할 것 같다
"""