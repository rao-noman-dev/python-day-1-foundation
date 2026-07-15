# Python Day 1 Foundation

A beginner-friendly Python project covering input/output, variables, data types, type conversion, arithmetic operations, testing, Git, GitHub, and a simple calculator mini project.

## Project Objectives

- Practice `print()` and `input()`
- Understand variables and comments
- Work with strings, integers, and floats
- Perform explicit type conversion
- Use addition, subtraction, multiplication, and division
- Build readable terminal programs
- Test normal and boundary inputs
- Track work with Git
- Publish the project on GitHub

## Project Structure

```text
python-backend-168-day-roadmap/
└── python-day-1/
    ├── day_1_exercises.py
    ├── calculator.py
    ├── notes.md
    ├── README.md
    └── DAY_1_HANDOFF.md
```

## Files

### `day_1_exercises.py`

Contains 15 beginner exercises:

1. Print name, city, and goal
2. Take a name and print a greeting
3. Add two numbers
4. Calculate next-year age
5. Calculate total marks
6. Calculate a product bill
7. Convert Celsius to Fahrenheit
8. Calculate rectangle area
9. Calculate yearly salary
10. Calculate the average of three numbers
11. Calculate marks percentage
12. Calculate discount and final price
13. Calculate simple interest
14. Convert hours to minutes and seconds
15. Calculate distance using speed and time

### `calculator.py`

Takes two numbers and displays:

- Addition
- Subtraction
- Multiplication
- Division

### `notes.md`

Contains Day 1 concepts, examples, testing observations, known limitations, and Git/GitHub learning notes.

### `DAY_1_HANDOFF.md`

Provides the exact Day 1 completion status and the starting point for the Day 2 agent.

## Requirements

- Python 3.x
- PowerShell or another terminal
- Visual Studio Code or another code editor
- Git
- GitHub account

No external Python packages are required.

## How to Run

Open PowerShell and move to the Day 1 project folder:

```powershell
Set-Location "C:\Users\User\Documents\python-backend-168-day-roadmap\python-day-1"
```

Run the Day 1 exercises:

```powershell
python .\day_1_exercises.py
```

Run the calculator mini project:

```powershell
python .\calculator.py
```

## Calculator Example

```text
Enter your first number: 5
Enter your second number: 3
Sum of two numbers is: 8.0
Subtraction of two numbers is: 2.0
Multiplication of two numbers is: 15.0
Division of two numbers is: 1.6666666666666667
```

## Testing Completed

The exercises and calculator were tested with:

- Positive integers
- Decimal numbers
- Negative numbers
- Zero as the first calculator number
- Formula-based expected outputs

## Known Limitations

### Division by Zero

Entering `0` as the second calculator number can raise:

```text
ZeroDivisionError: float division by zero
```

### Non-Numeric Input

Entering text such as `five` can raise:

```text
ValueError
```

### Floating-Point Precision

Some float calculations may display extra decimal digits. This is normal behavior.

## Git History

The repository uses separate Git commits for major Day 1 milestones:

- Day 1 Python exercises and calculator
- Day 1 documentation and handoff
- Local roadmap-folder path updates

To view the latest commit history, run:

```powershell
git log --oneline
```

## GitHub Repository

https://github.com/rao-noman-dev/python-day-1-foundation

## Learning Outcome

After completing Day 1, I can take and convert user input, store values in variables, perform arithmetic calculations, build and test a small command-line calculator, identify basic runtime limitations, use Git for version control, and publish a repository on GitHub.

## Author

**Rao Muhammad Noman**

GitHub: `rao-noman-dev`

## Project Status

Day 1 coding, testing, Git setup, GitHub publishing, and documentation are complete.
