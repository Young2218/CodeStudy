# 10912. 외로운 문자 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXVJuEvqLAADFASe
# 22.01.18

from string import ascii_lowercase

T = int(input())
for t in range(T):
    lines = list(input())

    for a in list(ascii_lowercase):
        while lines.count(a) >= 2:
            lines.remove(a)
            lines.remove(a)
    
    lines.sort()

    if len(lines) == 0:
        print(f'#{t+1} Good')
    else:
        result = ''.join(lines)
        print(f'#{t+1} {result}')