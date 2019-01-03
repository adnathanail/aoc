from aocd import get_data
inputstring = get_data(day=5, year=2015)
split = inputstring.split()
nicecount = 0
for line in split:
    vowelcount = 0
    for vowel in "aeiou":
        if vowel in line:
            vowelcount += line.count(vowel)
    double = False
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if (letter + letter) in line:
            double = True
    bannedcount = 0
    for bannedstring in ["ab", "cd", "pq", "xy"]:
        if bannedstring in line:
            bannedcount += 1
    if vowelcount >= 3 and double and bannedcount == 0:
        nicecount += 1
print(nicecount)
