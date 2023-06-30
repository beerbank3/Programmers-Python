def solution(my_string):
    answer = list(my_string.split(" "))
    answer = [item for item in answer if item != '']
    return answer