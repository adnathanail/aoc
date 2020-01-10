import numpy as np
from aocd import get_data
inp = get_data(day=3, year=2019)
inp = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""

class Grid:
  def __init__(self, *args):
    max_far_up = min_far_down = min_far_left = max_far_right = 0
    for line in args:
      far_up, far_down, far_left, far_right = self.get_bounds_of_line(line)
      max_far_up = max(max_far_up, far_up)
      min_far_down = min(min_far_down, far_down)
      min_far_left = min(min_far_left, far_left)
      max_far_right = max(max_far_right, far_right)
    self.height = max_far_up - min_far_down + 1
    self.width = max_far_right - min_far_left + 1
    self.center = (-far_left, -far_down)
    self.grid = np.zeros(shape=(self.height, self.width), dtype="U2")
    self.distance_grids = []

    for line in args:
      distance_grid = self.add_line(line)
      self.distance_grids.append(distance_grid)
  def get_bounds_of_line(self, line):
    far_up = far_down = 0
    far_left = far_right = 0
    x = y = 0
    for segment in line:
      direction = segment[0]
      distance = int(segment[1:])
      if direction == "U":
        y += distance
        far_up = max(y, far_up)
      elif direction == "D":
        y -= distance
        far_down = min(y, far_down)
      elif direction == "L":
        x -= distance
        far_left = min(x, far_left)
      elif direction == "R":
        x += distance
        far_right = max(x, far_right)
    return far_up, far_down, far_left, far_right
  def add_line(self, line):
    distance_grid = np.zeros(shape=(self.height, self.width))

    loc = self.center
    i = 0  # Distance from start
    for segment in line:
      direction = segment[0]
      distance = int(segment[1:])
      for _ in range(distance):
        i += 1
        if direction == "U":
          loc = (loc[0], loc[1]+1)
        elif direction == "D":
          loc = (loc[0], loc[1]-1)
        elif direction == "L":
          loc = (loc[0]-1, loc[1])
        elif direction == "R":
          loc = (loc[0]+1, loc[1])
        self.grid[loc[1]][loc[0]] += "X"
        if distance_grid[loc[1]][loc[0]] == 0:
          distance_grid[loc[1]][loc[0]] = i
    return distance_grid
  def get_crossovers(self):
    points = np.where(self.grid == "XX")
    return list(zip(points[1], points[0]))
  def get_fewest_combined_steps_to_crossover(self):
    return min([sum([dg[co[1]][co[0]] for dg in self.distance_grids]) for co in self.get_crossovers()])
  def print_grid(self):
    for row in self.grid[::-1]:
      print("".join([(x+"  ")[:2] for x in row]))

line1, line2 = [x.split(",") for x in inp.split("\n")]
g = Grid(line1, line2)
print(g.get_fewest_combined_steps_to_crossover())