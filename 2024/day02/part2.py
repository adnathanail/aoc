from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=2)
input_data = puzzle.input_data

reports = [[int(l) for l in r.split(" ")] for r in input_data.splitlines()]

def is_safe(report, dampers_left=True):
    # Make our life easy by normalising reports to always be increasing
    #   (e.g. if we receive [5, 4, 3, 2] we change it to [-5, -4, -3, -2])
    if report[0] > report[1]:
        report = [-x for x in report]

    for i in range(len(report) - 1):
        # If the distance between 2 levels isn't 1, 2, or 3
        if (report[i + 1] - report[i]) not in [1, 2, 3]:
            # Try damping if we can
            if dampers_left:
                # Try removing one of the two numbers causing problems and checking if either of those reports would be safe
                #   (remembering to set dampers_left to false, so the report is only damped once)
                if is_safe(report[:i] + report[i + 1:], dampers_left=False) or is_safe(report[:i + 1] + report[i + 2:], dampers_left=False):
                    return True
                else:
                    # Last resort, the issue may have been the first level, setting the increasing/decreasing direction incorrectly
                    return is_safe(report[1:], dampers_left=False)
            # Otherwise fail
            else:
                return False
    # If all the gaps were 1, 2 or 3 then return safe
    return True


num_safe_reports = 0

for r in reports:
    if is_safe(r):
        num_safe_reports += 1

print(num_safe_reports)
