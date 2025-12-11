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


def enrich_chars(list):
    enrich_dic = []
    for i in list:
        item = {"char": (i),"num": list[i]}
        enrich_dic.append(item)
    return enrich_dic

def sort_on(dictionary):
    return dictionary["num"]

def sort_count(new_char):
    new_char.sort(reverse=True, key=sort_on)
    for i in new_char:
        ch = i["char"]
        count = i["num"]
        if not ch.isalpha():
            continue
        print (f"{ch}: {count}")