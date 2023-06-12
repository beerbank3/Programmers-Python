def solution(s, skip, index):
    answer = ''
    skip_set = set(ord(char) for char in skip)
    for char in s:
        temp = ord(char)
        j = 0
        while j < index:
            temp += 1
            
            if temp > 122:
                temp -= 26
                
            if temp in skip_set:
                continue
            else:
                j += 1
        answer += chr(temp)

    return answer