from stats import get_dict_of_chars, get_num_words, get_sorted_char_dict
import sys

def get_book_test(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at {path}...".format(path=path_to_book))
    print("----------- Word Count ----------")
    print("Found {num_words} total words".format(num_words=get_num_words(path_to_book)))
    print(get_dict_of_chars(get_book_test(path_to_book)))
    print("----------- Character Count -----------")
    sorted_char_dict  = get_sorted_char_dict(get_dict_of_chars(get_book_test(path_to_book)))
    for item in sorted_char_dict:
        print("{char}: {num}".format(char=item["char"], num=item["num"]))
    print("============= END ===============")


main()