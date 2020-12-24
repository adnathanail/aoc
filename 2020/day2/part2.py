import re

from aocd import get_data

inp = get_data(day=2, year=2020)

r = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

valid_passwords = 0
for pw in inp.split("\n"):
  p1, p2, letter, string = re.match(r, pw).groups()
  if (string[int(p1) - 1] == letter) != (string[int(p2) - 1] == letter):  # XOR!!
    valid_passwords += 1

print(valid_passwords)
