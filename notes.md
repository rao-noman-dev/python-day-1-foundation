# Day 1 Python Notes

## `print()`

`print()` kisi statement, value, variable, ya calculation result ko terminal par display karne ke liye use hota hai.

```python
print("Hello, Python!")
```

## `input()`

`input()` user se data lene ke liye use hota hai. Python mein `input()` se milne wali value default tor par string hoti hai.

```python
user_name = input("Enter your name: ")
```

## Variables

Variable ek named container hota hai jisme value store hoti hai aur baad mein reuse ki ja sakti hai.

```python
city = "Lahore"
age = 18
```

## Comments

Comments code ko explain aur readable banane ke liye likhe jate hain. Python interpreter comments ko execute nahi karta.

```python
# This program calculates a total
```

## String Data Type

String text ko represent karti hai aur single ya double quotes mein likhi jati hai.

```python
name = "Rao Muhammad Noman"
goal = "Become a Python Backend Developer"
```

## Integer Data Type

Integer whole number hota hai jisme decimal point nahi hota.

```python
age = 18
quantity = 5
temperature = -10
```

## Float Data Type

Float decimal number hota hai.

```python
price = 99.50
height = 5.9
temperature = -3.5
```

## Type Conversion

Type conversion ka matlab ek data type ko doosre data type mein convert karna hai. Kyun ke `input()` string return karta hai, numeric calculation se pehle `int()` ya `float()` use kiya jata hai.

```python
age = int(input("Enter your age: "))
price = float(input("Enter product price: "))
```

## Arithmetic Operators

| Operator | Purpose | Example |
|---|---|---|
| `+` | Addition | `5 + 3` |
| `-` | Subtraction | `5 - 3` |
| `*` | Multiplication | `5 * 3` |
| `/` | Division | `5 / 3` |

## Day 1 Exercises

Day 1 mein 15 beginner exercises complete ki gayi jin mein input/output, type conversion, arithmetic calculations, percentages, conversions, aur practical formulas practice kiye gaye.

## Calculator Mini Project

Calculator do numbers leta hai, unko `float` mein convert karta hai, aur addition, subtraction, multiplication, aur division show karta hai.

## Floating-Point Precision

Python floats kabhi extra decimal digits show karte hain.

```text
5.9 - 9.032 = -3.1319999999999997
```

Mathematical result approximately `-3.132` hai. Yeh normal floating-point behavior hai.

## Division-by-Zero Risk

Second number `0` ho to division line `ZeroDivisionError` de sakti hai.

```python
division = num_1 / num_2
```

## Non-Numeric Input Limitation

Text input, jaise `five`, ko `float()` number mein convert nahi kar sakta aur `ValueError` aa sakta hai.

Valid examples:

```text
5
5.9
-10
0
```

## Git and GitHub

Day 1 project ko local Git repository banaya gaya, first commit create ki gayi, remote GitHub repository connect ki gayi, aur `main` branch successfully push ki gayi.

## What I Learned Today

- `print()` se output display karna
- `input()` se user data lena
- Variables mein values store karna
- Comments likhna
- `str`, `int`, aur `float` use karna
- Type conversion karna
- Basic arithmetic operations karna
- 15 beginner exercises complete karna
- Simple calculator build aur test karna
- Integer, decimal, negative, aur zero inputs test karna
- Floating-point precision, division-by-zero, aur non-numeric input limitations samajhna
- Git repository initialize, commit, remote connect, aur GitHub par push karna

## Problems I Faced Today

- Calculator mein addition ke liye galti se subtraction operator `-` use kar diya tha. Isay `+` se correct kiya.
- Multiplication output mein spelling mistake thi, jise correct kiya.
- Decimal calculations mein extra digits nazar aaye, jo Python floating-point precision ka normal behavior hai.
- GitHub push ke waqt wrong cached account ki wajah se `403 Permission Denied` error aaya. Windows Credential Manager se old GitHub credentials remove karke correct account se authentication complete ki.
- Project folder move karne ke baad `README.md` aur `DAY_1_HANDOFF.md` mein local paths update kiye.

## Next-Day Preparation

- Day 2 start karne se pehle `README.md`, `notes.md`, aur `DAY_1_HANDOFF.md` read karni hain.
- Day 1 repository ka branch, working-tree status, commits, remote, aur GitHub synchronization verify karni hai.
- Day 1 exercises aur calculator dobara rebuild nahi karne.
- Sirf official Day 2 roadmap scope follow karna hai.
- Day 2 ki documentation aur handoff files coding, testing, Git, GitHub, aur final verification ke baad end mein create karni hain.