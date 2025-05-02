import sys

from stats import get_book_text, get_number_char, get_number_words, listing


def main():
    try:
        path = sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print(sys.argv)
    text = get_book_text(path)
    print(f"Found {get_number_words(text)} total words")
    final = listing(path)
    for x in final:
        print(f"{x['char']}: {x['num']}")


main()
