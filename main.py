import stats
import sys

def get_book_text(path_to_file) :
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_file = sys.argv[1]
    book = get_book_text(book_file)
    book_words_count = stats.word_count(book)
    char_dict = stats.count_char(book)
    
    stats.print_results(book_file, book_words_count, char_dict)

main()