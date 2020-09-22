sentence = "This is a common interview question blablablablablablablablablablablaaaaaaaaaaaaa"

#Most repeated character in a text
def find_most_repeated_character_in_text(text):
    characters = [*text]
    #print(characters)
    characters_dic = {c:characters.count(c) for c in characters}
    #print(characters_dic)
    characters_dic_sorted = sorted(characters_dic.items(), key=lambda kv: kv[1], reverse=True)
    #print(characters_dic_sorted)
    return characters_dic_sorted[0]

result = find_most_repeated_character_in_text(sentence)
print(result)
print(result[0])
print(type(result))