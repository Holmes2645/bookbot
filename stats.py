def word_count(book):
    words = book.split()
    count = len(words)
    return count 

def count_char(book):
    char_dict = {}
    book = book.lower()
    words = book.split()

    for word in words:
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict 

def sort_on(dict):
        return dict[""]


def print_results(book,word_count,char_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

     
    # Sort the dict items by ascending frequency (value)
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)


    
    for char,freq in sorted_dict:
        print(f"{char}: {freq}")


   