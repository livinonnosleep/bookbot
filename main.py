def get_book_text(book):
    with open(book) as f:
        return f.read() 

from stats import count_words

from stats import char_count

from stats import sort_count

def main():
    book_path = ("books/frankenstein.txt")
    text = get_book_text(book_path)
    count = count_words(text)
    chars = char_count(text)
    #sort_count(chars)
    print (f"Found {count} total words")
    print (chars)
    #print (order_value)

main()