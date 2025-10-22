# skills-copilot-codespaces-vscode
My clone repository

## AI Math Helper

A Python chatbot that solves basic math and logic problems using SymPy and rule-based logic.

### Features

- **Arithmetic Calculations**: Perform basic arithmetic operations
  - Addition, subtraction, multiplication, division
  - Exponentiation (use `^` or `**`)
  - Examples: `2 + 2`, `5 * 3`, `2^3`

- **Algebraic Equations**: Solve equations with variables
  - Linear equations: `solve 2*x + 5 = 15`
  - Quadratic equations: `solve x^2 - 4 = 0`
  - Direct input: `x^2 + 2*x + 1 = 0`

- **Expression Simplification**: Simplify, expand, and factor algebraic expressions
  - `simplify (x+1)^2` → Shows simplified, expanded, and factored forms
  - `simplify x^2 - 1` → Factors as `(x-1)(x+1)`

- **Calculus Operations**:
  - **Derivatives**: `derivative of x^2`, `derivative of 2*x^3 + 3*x`
  - **Integrals**: `integrate x^2`, `integrate 2*x`

- **Logic Problems**: Solve basic logical reasoning problems
  - Conditional logic: `if A then B, A is true`
  - Conjunctions: `P and Q are both true`
  - Disjunctions: `A or B is false`
  - Supports Modus Ponens and Modus Tollens

### Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Usage

#### Interactive Mode

Run the chatbot in interactive mode:
```bash
python3 math_helper.py
```

Then enter your math or logic problems:
```
You: 2 + 2
AI: Result: 4 = 4.0

You: solve x^2 - 4 = 0
AI: Solutions for x:
  x = -2
  x = 2

You: derivative of x^2
AI: Derivative of x**2 with respect to x:
  d/dx = 2*x

You: if it rains then ground is wet, it rains is true
AI: Logic Analysis:
  Rule: If it rains then ground is wet
  Given: it rains is True
  Conclusion: ground is wet is TRUE (Modus Ponens)
```

Type `help` to see all available commands, or `quit` to exit.

#### Running Tests

To verify the chatbot functionality:
```bash
python3 test_math_helper.py
```

### Examples

**Arithmetic:**
- `2 + 2` → `4`
- `10 / 2` → `5`
- `2^3` → `8`

**Equations:**
- `solve x^2 - 4 = 0` → Solutions: x = -2, x = 2
- `solve 2*x + 5 = 15` → Solution: x = 5

**Simplification:**
- `simplify (x+1)^2` → Expands to `x^2 + 2*x + 1`
- `simplify x^2 - 1` → Factors to `(x-1)(x+1)`

**Calculus:**
- `derivative of x^2` → `2*x`
- `integrate x^2` → `x^3/3 + C`

**Logic:**
- `if A then B, A is true` → B is TRUE (Modus Ponens)
- `P and Q are both true` → P is TRUE, Q is TRUE

### Requirements

- Python 3.7+
- SymPy 1.12+

### License

This project is part of a GitHub Codespaces learning exercise.

