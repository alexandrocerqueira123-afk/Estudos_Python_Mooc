
#PROBLEM 1 - WORDS THAT BEGIN WITH VOWEL

word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
def begin_with_vowel(old_list:list):
    new_list = [word for word in old_list if word[0].lower() in 'aeiou']
    return new_list

print(begin_with_vowel(word_list))

print("\n\n\n")

#PROBLEM 2 - FORBIDDEN CHARACTER

def filter_forbbiden(sentence:str, characters:str):
    new_sentence = [character for character in sentence if character not in characters]
    return "".join(new_sentence)

sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbbiden(sentence, "!?:,.")
print(filtered)

print("\n\n\n")

#PROBLEM 3 - COUNTING CHARACTERS

sentence = "hello there"

char_counts = {character:sentence.count(character) for character in sentence}
print(char_counts)