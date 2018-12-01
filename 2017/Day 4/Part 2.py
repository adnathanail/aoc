from aocd import get_data
inp = [x.split() for x in get_data(day=4, year=2017).split('\n')]

def tally_word(word):
    d = {}
    for char in word:
        if char not in d:
            d[char] = 0
        d[char] += 1
    return d

def dict_identical(d1, d2):
    for k in d1.keys():
        if k not in d2:
            return False
        elif d1[k] != d2[k]:
            return False
        del d2[k]
    if len(d2.keys()) == 0:
        return True
    else:
        return False

def word_anagram(w1, w2):
    return dict_identical(tally_word(w1), tally_word(w2))        

def valid_password(p):
    used_words = []
    for word in p:
        if True in [word_anagram(word, uw) for uw in used_words]:
            return False
        used_words.append(word)
    return True

count = 0
for p in inp:
    if valid_password(p):
        count += 1

print(count)