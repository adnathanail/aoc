from aocd import get_data
inp = get_data(day=2, year=2019)

class SomethingWentWrong(Exception):
  pass

class Interpreter:
  def __init__(self, program):
    self.program = [int(x) for x in program.split(",")]
  def set_noun_verb(self, noun, verb):
    self.program[1] = noun
    self.program[2] = verb
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

# # From the below I determine
# # For 0,0 the output is 29,848
# # Increasing the noun increases the output by 307,200
# # Increasing the verb increases the output by 1
# for noun in range(0, 10):
#   for verb in range(0, 10):
#     interp = Interpreter(inp)
#     interp.set_noun_verb(noun=noun, verb=verb)
#     print(noun, verb, interp.run())

noun = (19690720-29848) // 307200
verb = (19690720-29848) % 307200

# # Just to check
# interp = Interpreter(inp)
# interp.set_noun_verb(noun=noun, verb=verb)

print(100*noun + verb)