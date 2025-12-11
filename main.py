def get_book_text(book):
    with open(book) as f:
        return f.read() 

from stats import count_words

from stats import char_count

from stats import sort_count

from stats import enrich_chars

def main():
    book_path = ("books/frankenstein.txt")
    text = get_book_text(book_path)
    count = count_words(text)
    chars = char_count(text)
    chars_enrich = enrich_chars(chars)
    #chars_org = sort_count(chars_enrich)
    #sort_count(chars)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {book_path}...")
    print ("----------- Word Count ----------")
    print (f"Found {count} total words")
    print ("--------- Character Count -------")
    chars_org = sort_count(chars_enrich)
    print ("============= END ===============")
    #print (order_value)

main()