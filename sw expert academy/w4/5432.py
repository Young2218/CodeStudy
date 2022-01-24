# 5432. 쇠막대기 자르기 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVl47b6DGMDFAXm&categoryId=AWVl47b6DGMDFAXm&categoryType=CODE&problemTitle=5432&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&
# 22.01.34

T = int(input())
for t in range(T):
    information = input()

    cnt = 0
    stack = []
    for i in information:
        if i == '(':
            stack.append(1)
        elif i == ')':
            if stack[-1] == 1:
                # lazor
                stack.pop()
                for idx in range(len(stack)):
                    stack[idx] += 1
            else:
                cnt += stack.pop()
    
    print(f'#{t+1} {cnt}')

"""
저번에 풀었던 후위표기식이 도움이 된 듯
스택으로 풀어서 쉽게 해결
"""