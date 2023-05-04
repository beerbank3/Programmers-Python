def solution(babbling):
    answer = 0
    word_list = ['aya','ye','woo','ma']
    for word in word_list:
        for i, babble in enumerate(babbling):
            if (word+word) in babble:
                continue
            babbling[i] = babble.replace(word,' ')
    for i in babbling:
        if not i.replace(' ', ''):
            answer += 1
    return answer