def solution(str1, str2):
    result = []
    # 두 문자열 중 짧은 길이를 구합니다.
    min_length = min(len(str1), len(str2))
    
    # 두 문자열 중 짧은 길이만큼 반복합니다.
    for i in range(min_length):
        result.append(str1[i])
        result.append(str2[i])
    
    # 남은 부분을 처리합니다.
    if len(str1) > min_length:
        result.append(str1[min_length:])
    elif len(str2) > min_length:
        result.append(str2[min_length:])
    
    # 결과 문자열을 반환합니다.
    return ''.join(result)