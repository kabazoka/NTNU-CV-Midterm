
def speak_pirate(sentence):
    words = sentence.split(' ')
    translated_words = []
    for word in words:
        new_word = ''
        if 'r' in word:
            if count(word, 'r') <= 5:
                new_word = word.replace('r', 'rrr')  
        else:
            new_word = word
        if new_word.endswith('ing'):
            new_word = new_word.replace('ing', 'in')
        if new_word.endswith('g'):
            new_word = new_word.replace('g', 'gh')
        if count(new_word, 'r') > 5:
                new_word = new_word.replace('rrrrrr', 'rrrrr')  
        translated_words.append(new_word)
    return f"aye {' '.join(translated_words)}"

def count(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count += 1
    return count

def main():
    sentence = "strawberry"
    translated_sentence = speak_pirate(sentence)
    print(translated_sentence)

main()
