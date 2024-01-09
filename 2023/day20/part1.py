from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2023, day=20)

modules = {}

for row in puzzle.examples[0].input_data.split("\n"):
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
    if module_type in ["flipflop", "conjunction", "none"]:
        assert len(destinations) == 1
    modules[module_name] = {"type": module_type, "dests": destinations}

for m in modules:
    if modules[m]["type"] == "flipflop":
        modules[m]["state"] = "low"
    elif modules[m]["type"] == "conjunction":
        states = {}
        for m2 in modules:
            if m in modules[m2]["dests"]:
                states[m2] = "low"
        modules[m]["states"] = states

pulses = [{"origin": "button", "dest": "broadcaster", "signal": "low"}]

while pulses:
    pulse = pulses.pop(0)
    print(f"{pulse['origin']} -{pulse['signal']}-> {pulse['dest']}")
    pulse_module = modules[pulse["dest"]]

    if pulse_module["type"] == "broadcaster":
        for dest in pulse_module["dests"]:
            pulses.append({"origin": pulse["dest"], "dest": dest, "signal": pulse["signal"]})
    elif pulse_module["type"] == "flipflop":
        if pulse["signal"] == "low":
            pulse_module["state"] = "low" if pulse_module["state"] == "high" else "high"
            pulses.append({"origin": pulse["dest"], "dest": pulse_module["dests"][0], "signal": pulse_module["state"]})
    elif pulse_module["type"] == "conjunction":
        pulse_module["states"][pulse["origin"]] = pulse["signal"]
        all_high = True
        for state in pulse_module["states"]:
            if pulse_module["states"][state] == "low":
                all_high = False
                break
        pulses.append({"origin": pulse["dest"], "dest": pulse_module["dests"][0], "signal": "low" if all_high else "high"})
    else:
        break
