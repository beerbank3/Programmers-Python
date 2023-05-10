def solution(numbers, hand):
    answer = ''
    pad = {1: [0, 0], 2: [0, 1], 3: [0, 2],4: [1, 0], 5: [1, 1], 6: [1, 2],7: [2, 0], 8: [2, 1], 9: [2, 2],'*':[3, 0], 0: [3, 1], '#': [3, 2]}
    L = pad['*']
    R = pad['#']
    for i in numbers:
        now = pad[i]
        if i in [1,4,7]:
            answer += "L"
            L = now
        elif i in [3,6,9]:
            answer += "R"
            R = now
        else:
            left = 0
            right = 0
            for x,y,z in zip(L,R,now):
                left += abs(x-z)
                right += abs(y-z)
            if left < right or (left == right and hand == 'left'):
                answer += "L"
                L = now
            else:
                answer += "R"
                R = now
    return answer