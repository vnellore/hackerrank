from collections import Counter

def number_needed(a, b):
    a_list = list(a.upper())
    b_list = list(b.upper())

    deletions = 0
    if len(a_list) > len(b_list):
        b_list_copy = list(b_list)
        for i in iter(b_list_copy):
            if (i in a_list):
                b_list.remove(i)
                a_list.remove(i)
        print(b_list_copy)

    else:
        a_list_copy = list(a_list)
        for i in iter(a_list_copy):
            if i in b_list:
                b_list.remove(i)
                a_list.remove(i)
        print(a_list_copy)

    print(a_list)
    print(b_list)

    deletions = len(a_list) + len(b_list)
    return deletions


def ransom_note(magazine, ransom):
    magazine_counter = Counter(magazine.split(" "))
    ransom_counter = Counter(ransom.split(" "))

    valid = True
    for x in ransom_counter.keys():
        if ransom_counter[x] > magazine_counter[x]:
            valid = False

    return valid
