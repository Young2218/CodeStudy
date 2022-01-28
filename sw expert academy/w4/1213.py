# 1213. [S/W 문제해결 기본] 3일차 - String D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14P0c6AAUCFAYi
# 22.01.27

T = 10
for t in range(T):
    input()
    search = list(input())
    sentence = input()

    cnt = 0
    for i in range(len(sentence)):
        isSame = True
        for s in search:
            if i >= len(sentence) or s != sentence[i]: 
                isSame = False
                break
            i += 1
        if isSame: cnt+=1
    
    print(f'#{t+1} {cnt}')
            
            

