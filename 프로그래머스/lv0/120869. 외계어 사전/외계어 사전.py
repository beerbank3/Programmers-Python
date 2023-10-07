def solution(spell, dic):
    spell_str = ''.join(sorted(spell))
    
    for word in dic:
        word_str = ''.join(sorted(word))
        
        if spell_str == word_str:
            return 1
    
    return 2