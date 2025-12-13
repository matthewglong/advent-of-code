# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a multi-year, multi-participant Advent of Code solutions repository. Solutions are organized by year and participant.

## Structure

```
/{year}/{participant}/day{NN}/day{NN}.py
```

Examples:
- `2025/matthew/day01/day01.py`
- `2025/abel/day05/day05.py`
- `2022/Matthew/day01/day01.py`

Each day's folder contains:
- `day{NN}.py` - Python solution file (often uses `# %%` cell markers for Jupyter/VS Code interactive execution)
- `day{NN}.txt` - Puzzle input data

## Running Solutions

Solutions are standalone Python scripts. Run from the day's directory:

```bash
cd 2025/matthew/day01
python day01.py
```

Many solutions use `# %%` cell markers and can be run interactively in VS Code's Python Interactive window or Jupyter.

## Common Dependencies

- `numpy` - Used for grid/matrix problems (Days 4, 6, etc.)
- Standard library only for most solutions

## Code Conventions

- Problem statements are included as docstrings at the top of each file
- Part 1 and Part 2 solutions typically appear sequentially in the same file
- Input files are read relative to the script location (e.g., `open("day01.txt")`)
