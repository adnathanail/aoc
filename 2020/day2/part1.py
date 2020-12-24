import re

from aocd import get_data

inp = get_data(day=2, year=2020)

r = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

valid_passwords = 0
for pw in inp.split("\n"):
  low, high, letter, string = re.match(r, pw).groups()
  letter_count = string.count(letter)
  if int(low) <= letter_count <= int(high):
    valid_passwords += 1

print(valid_passwords)
