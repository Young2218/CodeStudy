# 1225 암호생성기
# 2022.01.03

try:
    tc = int(input())
    while tc > 0:
        nums = list(map(int, input().split()))
        
        repeat = True
        idx = 0
        while repeat:
            for i in range(1,6):
                nums[idx % 8] -= i
                if nums[idx % 8] <= 0:
                    nums[idx % 8] = 0
                    repeat = False
                    break
                idx += 1
        
        result = ''
        for i in range(1,9):
            result = result +  ' ' + str(nums[(idx+i)%8])

        print('#{}{}'.format(tc, result))

        tc = int(input())
except:
    exit