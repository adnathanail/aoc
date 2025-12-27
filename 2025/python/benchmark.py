#!/usr/bin/env python3
"""Benchmark all Advent of Code 2025 Python solutions."""

import subprocess
import sys
import time
from pathlib import Path


def run_solution(script_path: Path) -> tuple[float, str, bool]:
    """Run a solution script and return (elapsed_time, output, success)."""
    start = time.perf_counter()
    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            timeout=300,
        )
        elapsed = time.perf_counter() - start
        output = result.stdout.strip()
        success = result.returncode == 0
        if not success:
            output = result.stderr.strip() or output
        return elapsed, output, success
    except subprocess.TimeoutExpired:
        return 300.0, "TIMEOUT", False
    except Exception as e:
        return 0.0, str(e), False


def format_time(seconds: float) -> str:
    """Format time in appropriate units."""
    if seconds < 0.001:
        return f"{seconds * 1_000_000:.1f}µs"
    elif seconds < 1:
        return f"{seconds * 1000:.2f}ms"
    else:
        return f"{seconds:.3f}s"


def main():
    script_dir = Path(__file__).parent
    days = sorted(script_dir.glob("day*/"))

    total_time = 0.0
    results = []

    print("Advent of Code 2025 - Python Benchmarks")
    print("=" * 50)

    for day_dir in days:
        day_num = day_dir.name

        for part in [1, 2]:
            script = day_dir / f"part{part}.py"
            if not script.exists():
                continue

            elapsed, output, success = run_solution(script)
            total_time += elapsed

            status = "OK" if success else "FAIL"
            time_str = format_time(elapsed)

            # Truncate output if too long
            display_output = output if len(output) < 30 else output[:27] + "..."

            results.append({
                "day": day_num,
                "part": part,
                "time": elapsed,
                "time_str": time_str,
                "output": display_output,
                "success": success,
            })

            print(f"{day_num} part{part}: {time_str:>10}  [{status}]  {display_output}")

    print("=" * 50)
    print(f"Total time: {format_time(total_time)}")


if __name__ == "__main__":
    main()
