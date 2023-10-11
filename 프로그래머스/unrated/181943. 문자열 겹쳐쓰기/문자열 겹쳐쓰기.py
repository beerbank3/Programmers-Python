def solution(my_string, overwrite_string, s):
    if s < 0 or s >= len(my_string):
        return my_string
    else:
        return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]