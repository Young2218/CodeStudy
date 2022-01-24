# 11856. 반반 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXjS1GXqZ8gDFATi
# 22.01.24

T = int(input())
for t in range(T):
    sentence = list(input())

    result = 'Yes'
    while len(sentence) > 0:
        s = sentence[0]
        if sentence.count(s) != 2:
            result = 'No'
            break
        else:
            sentence.remove(s)
            sentence.remove(s)
    
    print(f'#{t+1} {result}')

"""
쉬웠당
"""