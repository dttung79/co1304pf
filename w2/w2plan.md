## Week 2

### Variables

#### Assigning values to variables

*   Variables are assigned values using the `=` symbol.
*   This is different from mathematical equality; it means "is assigned the value."
*   Example: `course = "COMP1753"` assigns the string "COMP1753" to the variable `course`.

#### Reassigning variables

*   Variables can be assigned a new value at any point in the program.
*   The new value can be fixed or derived from user input.

#### Multiple variables

*   Programs can have many variables, each with its own name (label).
*   Example: `first_name`, `last_name`.

### Naming variables

#### Rules

*   Must start with a letter or underscore.
*   Cannot start with a number.
*   Can only contain letters, numbers, and underscores.
*   Case-sensitive (`name`, `Name`, and `NAME` are different).
*   Cannot be Python keywords (e.g., `from`, `import`, `if`, `else`, `True`, `False`).

#### Conventions

*   **Variables:** Start with lowercase, use underscores for multiple words (e.g., `first_name`).
*   **Constants:** Uppercase with underscores (e.g., `VAT_RATE`).
*   **Meaningful names:** Concise but descriptive (e.g., `age` not `a`).

### Data types

#### Strings

*   Represent text, enclosed in quotes.
*   Example: `"Hello, world!"`.

#### Integers

*   Represent whole numbers.
*   Example: `42`, `-10`, `0`.

#### Other types

*   Booleans (`True` or `False`)
*   Floating-point numbers (decimals)

### Converting between types

*   `int()` converts a string to an integer.
*   `str()` converts a number to a string.
*   Necessary for combining numbers and text in output.

### Operators

*   **String operators:** `+` for concatenation (joining strings).
*   **Numeric operators:** `+`, `-`, `*`, `/` for addition, subtraction, multiplication, and division.

### Input and output

*   `input()` gets keyboard input from the user.
*   `print()` displays output to the console. 

### Examples

*   `HelloWorld.py`: A simple program that prints "Hello, world!".
*   `HelloName.py`: Gets the user's name and prints a greeting.
*   `HelloAge.py`: Gets the user's age and prints it.
*   `HelloDOB.py`: Calculates the user's year of birth.