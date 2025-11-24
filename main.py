from stats import get_num_words, get_count_of_each_letter, sort_dict
import sys
def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
    path = sys.argv[1]
    book = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(book)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    letters = get_count_of_each_letter(book)
    sorted_dict = sort_dict(letters)
    for item in sorted_dict:
        if item["char"].isalpha():
            char = item["char"]
            num = item["num"]
            print(f"{char}: {num}")
    print("============= END ===============")

main()
