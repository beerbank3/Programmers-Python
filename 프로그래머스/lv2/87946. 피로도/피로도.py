from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for i in list(permutations(dungeons,len(dungeons))):
        n = k
        count = 0
        for x,y in i:
            if n >= x:
                n -= y
                count+=1
            if answer < count:
                answer = count
    return answer