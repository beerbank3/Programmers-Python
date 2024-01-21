def solution(myString, pat):
    length = len(myString)

    for i in range(length, 0, -1):
        if myString[:i].endswith(pat):
            return myString[:i]

    return ""