import re

from aocd import get_data

inp = get_data(day=4, year=2020)
inp = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f"""


def year_validate(val, low, high):
  if len(val) != 4:
    return False
  try:
    i = int(val)
  except ValueError:
    return False
  return low <= i <= high


def eyr(val):
  return year_validate(val, 2020, 2030)


def hgt(val):
  quan, unit = val[:-2], val[-2:]
  if unit not in ["cm", "in"]:
    return False
  try:
    i = int(quan)
  except ValueError:
    return False
  if unit == "cm":
    return 150 <= i <= 193
  else:
    return 59 <= i <= 76


def hcl(val):
  return bool(re.match(r"#[1-9a-f]{6}", val))


def pid(val):
  return bool(re.match(r"[0-9]{9}", val))


def byr(val):
  return year_validate(val, 1920, 2002)


def iyr(val):
  return year_validate(val, 2010, 2020)


def ecl(val):
  return val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def cid(_val):
  return True


validators = {'eyr': eyr, 'hgt': hgt, 'hcl': hcl, 'pid': pid, 'byr': byr, 'iyr': iyr, 'ecl': ecl, 'cid': cid}


def validate_passport(passport):
  return all(validators[key](passport[key]) for key in validators)


def reset_current_passport():
  return {key: "" for key in validators}


valid_passports = 0
current_passport = reset_current_passport()
for row in inp.split("\n"):
  if row == "":
    if validate_passport(current_passport):
      valid_passports += 1
    current_passport = reset_current_passport()
    continue
  this_row = {kv.split(":")[0]: kv.split(":")[1] for kv in row.split(" ")}
  current_passport = {**current_passport, **this_row}

if validate_passport(current_passport):
  valid_passports += 1

print(valid_passports)
