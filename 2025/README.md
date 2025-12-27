Did Python first, then came back and reimplemented in Rust

Python results:
```
Advent of Code 2025 - Python Benchmarks
==================================================
day01 part1:   137.37ms  [OK]  1195
day01 part2:   184.15ms  [OK]  6770
day02 part1:   577.37ms  [OK]  35367539282
day02 part2:     2.768s  [OK]  45814076230
day03 part1:   139.89ms  [OK]  357
day03 part2:   126.19ms  [OK]  173229689350551
day04 part1:   137.87ms  [OK]  1516
day04 part2:   694.63ms  [OK]  9122
day05 part1:   135.01ms  [OK]  770
day05 part2:   146.25ms  [OK]  357674099117260
day06 part1:   130.79ms  [OK]  6891729672676
day06 part2:   159.43ms  [OK]  9770311947567
day07 part1:   156.74ms  [OK]  1566
day07 part2:   137.55ms  [OK]  5921061943075
day08 part1:    34.188s  [OK]  57970
day08 part2:     1.523s  [OK]  8520040659
day09 part1:   347.88ms  [OK]  4776487744
day09 part2:   923.72ms  [OK]  1560299548
day10 part1:   144.10ms  [OK]  522
day10 part2:     5.027s  [OK]  18105
day11 part1:   138.35ms  [OK]  688
day11 part2:   137.19ms  [OK]  293263494406608
day12 part1:    21.050s  [OK]  536
==================================================
Total time: 69.110s
```

Rust results:
```
Day 01
------
Part 1: 1195 (78.5µs)
Part 2: 6770 (484.4µs)

Day 02
------
Part 1: 35367539282 (18.9ms)
Part 2: 45814076230 (414.5ms)

Day 03
------
Part 1: 17445 (34.7µs)
Part 2: 173229689350551 (135.5µs)

Day 04
------
Part 1: 1516 (983.7µs)
Part 2: 9122 (19.8ms)

Day 05
------
Part 1: 770 (158.8µs)
Part 2: 357674099117260 (216.5µs)

Day 06
------
Part 1: 6891729672676 (141.7µs)
Part 2: 9770311947567 (276.3µs)

Day 07
------
Part 1: 1566 (247.6µs)
Part 2: 5921061943075 (310.5µs)

Day 08
------
Part 1: 57970 (43.4ms)
Part 2: 8520040659 (161.8ms)

Day 09
------
Part 1: 4776487744 (143.4µs)
Part 2: 1560299548 (27.3ms)

Day 10
------
Part 1: 522 (1.2ms)
Part 2: 18105 (7.3s)

Day 11
------
Part 1: 688 (2.8ms)
Part 2: 293263494406608 (3.2ms)

Day 12
------
Part 1: 536 (666.6ms)
```