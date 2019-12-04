import numpy as np
from aocd import get_data
inp = get_data(day=3, year=2019)

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

    for line in args:
      self.add_line(line)
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
    center = self.center
    for segment in line:
      direction = segment[0]
      distance = int(segment[1:])
      for _ in range(distance):
        if direction == "U":
          center = (center[0], center[1]+1)
        elif direction == "D":
          center = (center[0], center[1]-1)
        elif direction == "L":
          center = (center[0]-1, center[1])
        elif direction == "R":
          center = (center[0]+1, center[1])
        self.grid[center[1]][center[0]] += "X"
  def get_crossovers(self):
    points = np.where(self.grid == "XX")
    return list(zip(points[1], points[0]))
  @staticmethod
  def get_manhattan_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)
  def get_distance_to_crossover_closest_to_center(self):
    return min([self.get_manhattan_distance(p, self.center) for p in self.get_crossovers()])
  def print_grid(self):
    for row in self.grid[::-1]:
      print("".join([(x+"  ")[:2] for x in row]))

line1, line2 = [x.split(",") for x in inp.split("\n")]
g = Grid(line1, line2)
# g.print_grid()
print(g.get_distance_to_crossover_closest_to_center())