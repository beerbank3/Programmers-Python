def solution(n, words):
    answer = [0,0]
    stack = []
    for i in range(len(words)):
        if stack.count(words[i]):
            answer = [(i%n)+1,(i//n)+1]
            break
        if stack and stack[-1][-1] != words[i][0]:
            answer = [(i%n)+1,(i//n)+1]
            break
        stack.append(words[i])
    
    return answer