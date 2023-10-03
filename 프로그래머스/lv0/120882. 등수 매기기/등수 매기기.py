def solution(score):
    def calculate_average(student):
        return sum(student) / len(student)
    
    averages = [(i, calculate_average(student)) for i, student in enumerate(score)]
    
    averages.sort(key=lambda x: x[1], reverse=True)
    
    ranks = [0] * len(score)
    rank = 1
    
    for i in range(len(averages)):
        if i > 0 and averages[i][1] != averages[i-1][1]:
            rank = i + 1
        ranks[averages[i][0]] = rank
    
    return ranks