## Week 3

### Conditional Statements

#### Introduction to Conditionals

- A conditional statement allows a program to make decisions.
- It checks if a condition is `True` and executes the corresponding block of code.
- Example:
  ```python
  if age >= 18:
      print("You are an adult.")
  ```

### The `if` Statement

- The basic conditional structure in Python.
- Syntax:
  ```python
  if condition:
      statement
  ```
- Example:
  ```python
  if score > 50:
      print("You passed!")
  ```

### The `else` Statement

- Provides an alternative action if the `if` condition is `False`.
- Syntax:
  ```python
  if condition:
      statement_if_true
  else:
      statement_if_false
  ```
- Example:
  ```python
  if age >= 18:
      print("You can vote.")
  else:
      print("You are too young to vote.")
  ```

### The `elif` Statement

- Used to check multiple conditions in sequence.
- Syntax:
  ```python
  if condition1:
      statement1
  elif condition2:
      statement2
  else:
      statement3
  ```
- Example:
  ```python
  if grade >= 90:
      print("A")
  elif grade >= 80:
      print("B")
  elif grade >= 70:
      print("C")
  else:
      print("Fail")
  ```

### Comparison Operators

- Used to compare values in conditions.
- Operators:
  - `==` (equal to)
  - `!=` (not equal to)
  - `>` (greater than)
  - `<` (less than)
  - `>=` (greater than or equal to)
  - `<=` (less than or equal to)
- Example:
  ```python
  if temperature > 30:
      print("It's hot outside!")
  ```

### Logical Operators

- Allow combining multiple conditions.
- Operators:
  - `and` (both conditions must be `True`)
  - `or` (at least one condition must be `True`)
  - `not` (negates a condition)
- Example:
  ```python
  if age >= 18 and has_id:
      print("You can enter.")
  ```

### Boolean Data Type

- Boolean values are `True` or `False`.
- Used in conditions for decision-making.
- Example:
  ```python
  is_raining = True
  if is_raining:
      print("Take an umbrella!")
  ```

### Input Validation with Conditionals

- Conditionals can check if user input is valid before proceeding.
- Example:
  ```python
  age = int(input("Enter your age: "))
  if age < 0:
      print("Invalid age.")
  else:
      print("Age recorded.")
  ```

### Nested Conditionals

- `if` statements can be placed inside other `if` statements.
- Example:
  ```python
  if age >= 18:
      if has_ticket:
          print("You can watch the movie.")
      else:
          print("You need a ticket.")
  else:
      print("You are too young for this movie.")
  ```

### Defensive Programming

- Ensuring programs handle unexpected inputs correctly.
- Example:
  ```python
  operation = input("Enter +, -, * or /: ")
  if operation in ["+", "-", "*", "/"]:
      print(f"You chose {operation}.")
  else:
      print("Invalid operation.")
  ```

### Examples

- **Simple Calculator**: A program that asks for two numbers and an operation, then performs the corresponding operation.
- **Age Validator**: Asks for the user's age and categorizes them as a child, teenager, or adult.
- **Discount Eligibility**: Determines if a user gets a discount based on student status or age.