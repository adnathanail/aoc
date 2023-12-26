from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2023, day=19)


def get_workflows_and_parts(inp):
    workflow_str, parts_str = inp.split("\n\n")

    workflows = {}

    for wf in workflow_str.split("\n"):
        wf_name, rest = wf.split("{")
        rest = rest[:-1]

        rules = []
        for rule in rest.split(","):
            if ":" in rule:
                rest, after_rule = rule.split(":")
                rules.append((rest[0], rest[1], int(rest[2:]), after_rule))
            else:
                rules.append((rule,))
        workflows[wf_name] = rules

    # print(workflows)

    parts = []
    for part in parts_str.split("\n"):
        x, m, a, s = re.match("\{x=(\d+).*,m=(\d+),a=(\d+),s=(\d+)\}", part).groups()
        parts.append({"x": int(x), "m": int(m), "a": int(a), "s": int(s)})

    return workflows, parts


def check_part(part, workflows):
    wf_name = "in"
    while True:
        # print("\t", wf_name)
        if wf_name in ["A", "R"]:
            return True if wf_name == "A" else False
        wf = workflows[wf_name]
        for rule in wf:
            # print("\t\t", rule)
            if len(rule) == 4:
                matches1 = rule[1] == "<" and part[rule[0]] < rule[2]
                matches2 = rule[1] == ">" and part[rule[0]] > rule[2]
                if matches1 or matches2:
                    # print("\t\t\t", "Matches")
                    wf_name = rule[3]
                    break
                # else:
                # print("\t\t\t", "Doesn't match")
            else:
                # print("\t\t\t", rule[0])
                wf_name = rule[0]
                break


def score_part(part):
    return part["x"] + part["m"] + part["a"] + part["s"]


wfs, ps = get_workflows_and_parts(puzzle.input_data)

tot = 0

for p in ps:
    if check_part(p, wfs):
        tot += score_part(p)

print(tot)
