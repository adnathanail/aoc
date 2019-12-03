from aocd import get_data
inp = get_data(day=2, year=2019)
class SomethingWentWrong(Exception):
  pass

class Interpreter:
  def __init__(self, program):
    self.program = [int(x) for x in program.split(",")]
  def pa1202(self):  # Program Alarm 1202
    self.program[1] = 12
    self.program[2] = 2
  def run(self):
    i = 0
    running = True
    last_written = None
    while i < len(self.program) and running:
      opcode = self.program[i]
      if opcode == 99:
        running = False
      elif opcode == 1:
        a, b, c = self.program[i+1:i+4]
        self.program[c] = self.program[a] + self.program[b]
        last_written = self.program[c]
        i += 4
      elif opcode == 2:
        a, b, c = self.program[i+1:i+4]
        self.program[c] = self.program[a] * self.program[b]
        last_written = self.program[c]
        i += 4
      else:
        raise SomethingWentWrong
    return last_written

interp = Interpreter(inp)
interp.pa1202()
print(interp.run())