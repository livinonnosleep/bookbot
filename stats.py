def count_words(textstring):
    words = textstring.split()
    return len(words)


def char_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dictionary):
    return dictionary[0]

def sort_count(char):
    char.sort(reverse=True, key=sort_on)
    print (char)