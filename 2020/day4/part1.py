from aocd import get_data

inp = get_data(day=4, year=2020)

required_fields = {'eyr', 'hgt', 'hcl', 'pid', 'byr', 'iyr', 'ecl'}

valid_passports = 0
current_passport = set()
for row in inp.split("\n"):
  if row == "":
    if current_passport.intersection(required_fields) == required_fields:
      valid_passports += 1
    current_passport = set()
    continue
  current_passport = current_passport.union({kv.split(":")[0] for kv in row.split(" ")})

print(valid_passports)
