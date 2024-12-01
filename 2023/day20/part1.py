from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2023, day=20)


def parse_modules(module_str):
    out = {}

    for row in module_str.split("\n"):
        module_details, destinations_str = row.split(" -> ")
        if module_details == "broadcaster":
            module_type = "broadcaster"
            module_name = "broadcaster"
        elif module_details[0] == "%":
            module_type = "flipflop"
            module_name = module_details[1:]
        elif module_details[0] == "&":
            module_type = "conjunction"
            module_name = module_details[1:]
        else:
            module_type = "none"
            module_name = module_details
        destinations = destinations_str.split(", ")
        if module_type == "none":
            assert len(destinations) == 1
        out[module_name] = {"type": module_type, "dests": destinations}

    # Deal with modules that are only mentioned as a destination
    modules_to_add = []
    for m in out:
        for d in out[m]["dests"]:
            if d not in out:
                modules_to_add.append(d)

    for m in modules_to_add:
        out[m] = {"type": "none", "dests": []}

    # Set initial states of modules (done separately, because we don't know what states a conjunction might need until all modules are loaded)
    for m in out:
        if out[m]["type"] == "flipflop":
            out[m]["state"] = "low"
        elif out[m]["type"] == "conjunction":
            states = {}
            for m2 in out:
                if m in out[m2]["dests"]:
                    states[m2] = "low"
            out[m]["states"] = states
        elif out[m]["type"] == "none":
            out[m]["state"] = ""

    return out


class RXGotTheMessage(Exception):
    pass


def press_button(ms, ps):
    num_low = 0
    num_high = 0

    while ps:
        # Get next pulse
        pulse = ps.pop(0)
        if pulse["dest"] == "rx" and pulse["signal"] == "low":
            raise RXGotTheMessage()
        if pulse["signal"] == "low":
            num_low += 1
        else:
            num_high += 1
        # print(f"{pulse['origin']} -{pulse['signal']}-> {pulse['dest']}")
        pulse_module = ms[pulse["dest"]]

        # Broadcast pulse
        if pulse_module["type"] == "broadcaster":
            for dest in pulse_module["dests"]:
                ps.append({"origin": pulse["dest"], "dest": dest, "signal": pulse["signal"]})
        # Flip-flop pulse
        elif pulse_module["type"] == "flipflop":
            if pulse["signal"] == "low":
                pulse_module["state"] = "low" if pulse_module["state"] == "high" else "high"
                for dest in pulse_module["dests"]:
                    ps.append({"origin": pulse["dest"], "dest": dest, "signal": pulse_module["state"]})
        # Conjunction pulse
        elif pulse_module["type"] == "conjunction":
            pulse_module["states"][pulse["origin"]] = pulse["signal"]
            all_high = True
            for state in pulse_module["states"]:
                if pulse_module["states"][state] == "low":
                    all_high = False
                    break
            for dest in pulse_module["dests"]:
                ps.append({"origin": pulse["dest"], "dest": dest, "signal": "low" if all_high else "high"})
        # Untyped pulse
        else:
            pulse_module["state"] = pulse["signal"]

    return num_low, num_high


modules = parse_modules(puzzle.input_data)

i = 0
while True:
    i += 1
    try:
        press_button(modules, [{"origin": "button", "dest": "broadcaster", "signal": "low"}])
    except RXGotTheMessage:
        break

print(i)

# total_low = 0
# total_high = 0

# for i in range(1000):
#     l, h = press_button(modules, [{"origin": "button", "dest": "broadcaster", "signal": "low"}])
#     total_low += l
#     total_high += h

# print(total_low * total_high)
