def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def get_number_words(text):
    split = text.split()
    num = len(split)
    return num


def get_number_char(path):
    count = {}
    with open(path) as f:
        file_contents = f.read()
        low = file_contents.lower()
        for char in low:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
    return count


def sort_on(final):
    return final["num"]


def listing(path):
    count = get_number_char(path)
    final = []
    for c in count:
        if c.isalpha():
            final.append({"char": c, "num": count[c]})
    final.sort(reverse=True, key=sort_on)
    return final
