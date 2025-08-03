def get_num_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return len(file_contents.split())
    
def get_dict_of_chars(text):
    char_dict = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            char_dict[char] = char_dict.get(char, 0) + 1
        else:
            char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def sort_on(items):
    return items["num"]

def get_sorted_char_dict(dic):
    key_value_pairs = []
    for key in dic:
        if key.isalpha():
            key_value_pairs.append({"char": key, "num": dic[key]})
    key_value_pairs.sort(reverse=True, key=sort_on)
    return key_value_pairs