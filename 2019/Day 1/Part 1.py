from aocd import get_data
inp = get_data(day=1, year=2019)

def fuel_from_mass(mass):
  return int(mass/3) - 2

print(sum([fuel_from_mass(int(m)) for m in inp.split("\n")]))