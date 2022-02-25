# 3124. 최소 스패닝 트리 D4
# 22.02.24

# 크루스칼 방식으로 풀어보자

def get_parents(child) -> int:
    if child == parents[child]: return child
    else: return get_parents(parents[child])

T = int(input())
for t in range(1,T+1):
    V, E = map(int, input().split())
    
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key = lambda x: x[2])
    parents = [i for i in range(V+1)]
    answer = 0
    
    for e in edges:        
        a,b,c = e
        a_parent = get_parents(a)
        b_parent = get_parents(b)

        if a_parent == b_parent: continue
        answer += c
        if a_parent < b_parent: parents[b_parent] = a_parent
        else: parents[a_parent] = b_parent

    print(f'#{t} {answer}')

"""
크루스칼은 사이클을 판단해야한다 잊지 말자
시간초과와 정답 0개
"""

"""
인터넷에 있는 것을 한 번 보고 베낌
람다 소팅을 잘쓰는 것이 코딩을 간편하게 할 수 있는 길인 것 같다
"""