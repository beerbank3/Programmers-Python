def solution(my_string, m, c):
    result = ""
    
    # 문자열의 길이를 계산합니다.
    length = len(my_string)
    
    # 세로로 c번째 열에 해당하는 글자들을 추출합니다.
    for i in range(c - 1, length, m):
        result += my_string[i]
    
    return result