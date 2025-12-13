# [Advent of code](https://adventofcode.com/) solutions

My solutions are written using Python 3.12.

I'm using [uv](https://docs.astral.sh/uv/) to manage my environment and run my code.

I'm using a library called `advent-of-code-data` to load my inputs automatically.

_Code from before 2024 has not been tested with uv or Python 3.12 so it might not work perfectly_

## Setup
```shell
brew install uv
uv sync
```

## Running a solution
```shell
uv run 2024/day01/part1.py
```

## Profiling a solution
```shell
python3 -m cProfile -o program.prof ./2025/day10/part2.py

```