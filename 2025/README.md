Did Python first, then came back and reimplemented in Rust

Python results:
```
Advent of Code 2025 - Python Benchmarks
==================================================
day01 part1:   135.01ms  [OK]  1195
day01 part2:   209.88ms  [OK]  6770
day02 part1:   570.56ms  [OK]  35367539282
day02 part2:     2.708s  [OK]  45814076230
day03 part1:   138.60ms  [OK]  17445
day03 part2:   129.37ms  [OK]  173229689350551
day04 part1:   140.41ms  [OK]  1516
day04 part2:   673.16ms  [OK]  9122
day05 part1:   135.81ms  [OK]  770
day05 part2:   147.98ms  [OK]  357674099117260
day06 part1:   126.92ms  [OK]  6891729672676
day06 part2:   133.15ms  [OK]  9770311947567
day07 part1:   153.59ms  [OK]  1566
day07 part2:   133.34ms  [OK]  5921061943075
day08 part1:    31.904s  [OK]  57970
day08 part2:     1.525s  [OK]  8520040659
day09 part1:   359.96ms  [OK]  4776487744
day09 part2:   920.00ms  [OK]  1560299548
day10 part1:   147.27ms  [OK]  522
day10 part2:     4.961s  [OK]  18105
day11 part1:   131.91ms  [OK]  688
day11 part2:   124.91ms  [OK]  293263494406608
day12 part1:    20.914s  [OK]  536
==================================================
Total time: 66.524s
```

Rust results:

| Day | Part 1 | Part 2 |
| :---: | :---: | :---:  |
| [Day 1](./rust/src/bin/01.rs) | `57.1µs` | `353.8µs` |
| [Day 2](./rust/src/bin/02.rs) | `18.5ms` | `419.2ms` |
| [Day 3](./rust/src/bin/03.rs) | `24.3µs` | `96.2µs` |
| [Day 4](./rust/src/bin/04.rs) | `978.0µs` | `19.8ms` |
| [Day 5](./rust/src/bin/05.rs) | `144.5µs` | `211.2µs` |
| [Day 6](./rust/src/bin/06.rs) | `123.3µs` | `249.4µs` |
| [Day 7](./rust/src/bin/07.rs) | `210.3µs` | `274.0µs` |
| [Day 8](./rust/src/bin/08.rs) | `42.3ms` | `166.3ms` |
| [Day 9](./rust/src/bin/09.rs) | `118.8µs` | `24.8ms` |
| [Day 10](./rust/src/bin/10.rs) | `1.2ms` | `7.2s` |
| [Day 11](./rust/src/bin/11.rs) | `2.8ms` | `2.7ms` |
| [Day 12](./rust/src/bin/12.rs) | `621.2ms` | `-` |

**Total: 8521.64ms**