from stats import get_num_words, get_count_of_each_letter, sort_dict
def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book = get_book_text("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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
