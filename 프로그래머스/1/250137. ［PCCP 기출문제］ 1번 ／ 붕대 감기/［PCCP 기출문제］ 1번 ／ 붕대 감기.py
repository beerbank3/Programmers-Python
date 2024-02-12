def solution(bandage, health, attacks):
    answer = health
    index = 0
    length = attacks[-1][0]
    for i in range(1,length+1):
        if attacks[0][0] == i:
            answer -= attacks[0][1]
            attacks.pop(0)
            index = 0
            if answer < 1:
                return -1
            continue
        answer += bandage[1]
        index += 1
        if bandage[0] == index:
            answer += bandage[2]
            index = 0
        if answer > health:
            answer = health
    if answer < 1:
        return -1
    return answer