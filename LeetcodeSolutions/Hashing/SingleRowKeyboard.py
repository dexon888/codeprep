def singleRowKeyboard(keyboard, word):
    index = 0
    map = {}
    for i,c in enumerate(keyboard):
        map[c] = i
    
    result = 0
    for c in word:
        result += abs(map[c] - index)
        index = map[c]
    return result

keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"
print(singleRowKeyboard(keyboard, word))