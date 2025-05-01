def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def get_number_words(text):
    split = text.split()
    num = len(split)
    return num


def get_number_char(filepath):
    count = {}
    with open(filepath) as f:
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

def listing(filepath):
    count = get_number_char(filepath)
    final = []
    for c in count:
        if c.isalpha():
        	final.append({"char" :c, "num" :count[c]})
    final.sort(reverse=True, key=sort_on)
    return final
