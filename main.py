from stats import get_book_text, get_number_char, get_number_words, listing


def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num = get_number_words(text)
    print(get_number_char(filepath))
    print(f"{num} words found in the document")
    print(listing(filepath))

main()
