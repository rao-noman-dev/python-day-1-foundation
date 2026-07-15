# Day 1 Handoff

## Purpose

This file provides the complete Day 1 status for the next agent. Day 1 work is complete after the final documentation commit and GitHub push are verified.

## Learner

- Name: Rao Muhammad Noman
- GitHub username: `rao-noman-dev`
- Learning goal: Become a Python Backend Developer
- Preferred guidance style: Beginner-friendly, practical, step-by-step, Roman Urdu
- Important workflow preference: Create `notes.md`, `README.md`, and the day-specific handoff file only at the very end after coding, testing, Git, GitHub, and verification are complete.

## Local Environment

- Operating system: Windows
- Shell: Windows PowerShell 5.1
- Python: 3.13.7
- VS Code: 1.127.0 x64
- Git: 2.55.0.windows.2
- Local project path: `C:\Users\User\Documents\python-day-1`
- Git branch: `main`

## GitHub Repository

- Repository: `rao-noman-dev/python-day-1-foundation`
- Repository URL: https://github.com/rao-noman-dev/python-day-1-foundation
- Visibility: Public
- Remote name: `origin`
- Remote URL: `https://github.com/rao-noman-dev/python-day-1-foundation.git`

## Completed Files

### `day_1_exercises.py`

Contains 15 beginner exercises covering:

1. Printing name, city, and goal
2. Name input and greeting
3. Sum of two numbers
4. Next-year age
5. Marks total
6. Product bill
7. Celsius-to-Fahrenheit conversion
8. Rectangle area
9. Monthly and yearly salary
10. Average of three numbers
11. Marks percentage
12. Discount and final price
13. Simple interest and final amount
14. Hours to minutes and seconds
15. Distance using speed and time

### `calculator.py`

A learner-written simple calculator that accepts two `float` inputs and prints:

- Addition
- Subtraction
- Multiplication
- Division

### Final documentation files

- `notes.md`
- `README.md`
- `DAY_1_HANDOFF.md`

## Testing Completed

Verified calculator tests:

### Positive integers

```text
Input: 5, 3
Addition: 8.0
Subtraction: 2.0
Multiplication: 15.0
Division: 1.6666666666666667
```

### Decimal values

```text
Input: 5.9, 9.032
Addition: 14.932
Subtraction: -3.1319999999999997
Multiplication: 53.2888
Division: 0.6532329495128433
```

### Negative value

```text
Input: -10, 2
Addition: -8.0
Subtraction: -12.0
Multiplication: -20.0
Division: -5.0
```

### Zero as first number

```text
Input: 0, 5
Addition: 5.0
Subtraction: -5.0
Multiplication: 0.0
Division: 0.0
```

Individual exercises were also tested with representative valid values and produced correct expected outputs.

## Known Limitations

- `input()` returns a string by default.
- Numeric input is converted using `int()` or `float()`.
- Non-numeric text can raise `ValueError`.
- Dividing by zero can raise `ZeroDivisionError`.
- Float calculations may display precision artifacts such as `-3.1319999999999997`.
- No conditions, loops, classes, external packages, or advanced exception handling were introduced on Day 1.

## Git Status Before Final Documentation

Verified code commit:

```text
2ade931 Add Day 1 Python exercises and calculator
```

Verified status before documentation creation:

```text
On branch main
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

Verified tracking:

```text
main -> origin/main
```

## Final Day 1 Steps

After placing this handoff file, `notes.md`, and `README.md` in the project folder:

1. Review all three documentation files.
2. Run `git status`.
3. Stage the three documentation files.
4. Create a final documentation commit.
5. Push `main` to `origin`.
6. Verify the working tree is clean and local `main` matches `origin/main`.

## Exact Starting Point for Day 2 Agent

1. Read `README.md`, `notes.md`, and `DAY_1_HANDOFF.md`.
2. Verify the local repository path and run:

```powershell
git status
git branch -vv
git log --oneline -2
```

3. Confirm the Day 1 repository is clean and synchronized with GitHub.
4. Do not repeat Day 1 exercises or rebuild the calculator.
5. Start only the official Day 2 roadmap scope.
6. Continue using small checkpoints with actual terminal-output verification.
7. Keep instructions beginner-friendly and explain every new terminal command.
8. Create Day 2 documentation and handoff files only at the very end of Day 2.
