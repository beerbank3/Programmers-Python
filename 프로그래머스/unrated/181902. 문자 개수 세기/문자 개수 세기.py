def solution(my_string):
    alphabet_count = [0] * 52
    
    for char in my_string:
        if 'A' <= char <= 'Z':
            index = ord(char) - ord('A')
            alphabet_count[index] += 1
        elif 'a' <= char <= 'z':
            index = ord(char) - ord('a') + 26
            alphabet_count[index] += 1
    
    return alphabet_count
