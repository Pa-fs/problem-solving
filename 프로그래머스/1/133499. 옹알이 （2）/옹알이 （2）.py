def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    banned_words = ["ayaaya", "yeye", "woowoo", "mama"]
    for actual_word in babbling:
        for banned_word in banned_words:
            actual_word = actual_word.replace(banned_word, "x")
        for word in words: 
            actual_word = actual_word.replace(word, "0")
        
        if actual_word.isdigit():
            answer = answer + 1
        
    return answer