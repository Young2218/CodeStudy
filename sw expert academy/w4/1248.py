# 1248. [S/W 문제해결 응용] 3일차 - 공통조상 D5
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15PTkqAPYCFAYD
# 22.01.27


def sum_children(now) -> int:
    global children

    if now not in children: return 1
    result = 1
    for c in children[now]:
        result += sum_children(c)
    return result

T = int(input())
for t in range(T):
    V, E, a, b = map(int, input().split())
    infor = list(map(int,input().split()))

    mom = {}
    children = {}

    for i in range(0,2*E,2):
        if infor[i] in children:
            children[infor[i]].append(infor[i+1])
        else:
            children[infor[i]] = [infor[i+1]]
        
        mom[infor[i+1]] = infor[i]

    # 공통조상 찾기
    a_ancestor = []
    temp = a
    while temp in mom:
        a_ancestor.append(mom[temp])
        temp = mom[temp]
    
    temp = b
    while True:
        if mom[temp] in a_ancestor:
            both_ancestor = mom[temp]
            break
        temp = mom[temp]
    
    babys = sum_children(both_ancestor)

    print(f'#{t+1} {both_ancestor} {babys}')