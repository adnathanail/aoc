from functools import cache

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=11)
# inp = """svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out"""
inp = puzzle.input_data

cables = {}
for row in inp.splitlines():
    cable_from, cable_to_str = row.split(": ")
    cables[cable_from] = cable_to_str.split(" ")

@cache
def follow_cables(start_cable, end_cable, *, seen_fft=False, seen_dac=False):
    out = 0
    for c in cables[start_cable]:
        if c == end_cable:
            if seen_fft and seen_dac:
                out += 1
            else:
                continue
        else:
            out += follow_cables(c, end_cable, seen_fft=seen_fft or c == "fft", seen_dac=seen_dac or c == "dac")
    return out

print(follow_cables("svr", "out"))