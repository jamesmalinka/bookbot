def main():
    bookpath = "books/frankenstein.txt"
    print(f"--- Begin report of {bookpath} ---")
    print(f"{word_count(bookpath)} words found in the document\n")
    # print character count
    char_report(count_characters(bookpath))
    print("--- End report ---")


def get_text(bookfile):
    with open(bookfile) as f:
        return f.read()

def word_count(bookfile):
    book_text = get_text(bookfile)
    words_doc = book_text.split()
    wc = len(words_doc)
    return wc

def count_characters(bookfile):
    lowercased_book = get_text(bookfile).lower()
    characters_counted = {}
    for character in lowercased_book:
        if character in characters_counted:
            characters_counted[character] += 1
        elif character not in characters_counted:
            characters_counted[character] = 1
    return characters_counted

def sort_on(dict):
    return dict["number"]

def char_report(dicto):
    biglist = []
    for x in dicto:
        if x.isalpha():
            biglist.append({"letter": x, "number": dicto[x]})
    #sorton
    biglist.sort(reverse=True, key=sort_on)
    for i in range(0,len(biglist)):
        print(f"The '{biglist[i]["letter"]}' character was found {biglist[i]["number"]} times")
        


main()