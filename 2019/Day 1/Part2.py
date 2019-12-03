from aocd import get_data
inp = get_data(day=1, year=2019)

def fuel_from_mass(mass):
  ffm = int(mass/3) - 2
  if ffm <= 0:
    return 0
  else:
    return ffm + fuel_from_mass(ffm)

print(sum([fuel_from_mass(int(m)) for m in inp.split("\n")]))