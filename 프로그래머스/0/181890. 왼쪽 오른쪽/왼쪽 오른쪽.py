def solution(str_list):
    answer = []
    for index, str in enumerate(str_list):
        if str == 'l':
            answer = str_list[0:index]
            break
        elif str == 'r':
            answer = str_list[index+1:]
            break
    return answer