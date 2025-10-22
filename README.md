# skills-copilot-codespaces-vscode
My clone repository

## AI Math Helper 🤖

A beginner-friendly command-line math assistant that helps solve basic arithmetic expressions and simple algebraic equations.

### Features

- **Arithmetic Expression Solver**: Evaluate mathematical expressions with proper operator precedence
- **Algebraic Equation Solver**: Solve simple equations for variable `x`
- **History Tracking**: Automatically saves all solved problems to `math_history.txt` with timestamps
- **User-Friendly Interface**: Menu-driven with emoji indicators and helpful error messages
- **Error Handling**: Gracefully handles invalid inputs with helpful tips

### Installation

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the program:
```bash
python3 ai_math_helper.py
```

Or make it executable and run directly:
```bash
chmod +x ai_math_helper.py
./ai_math_helper.py
```

### Examples

#### Arithmetic Operations
```
Enter an arithmetic expression (e.g., 3 + 5 * 2): 3 + 5 * 2
✅ Result: 3 + 5 * 2 = 13.0

Enter an arithmetic expression (e.g., 3 + 5 * 2): (15 + 25) / 2
✅ Result: (15 + 25) / 2 = 20.0

Enter an arithmetic expression (e.g., 3 + 5 * 2): 2**10
✅ Result: 2**10 = 1024.0
```

#### Algebraic Equations
```
Enter an equation (e.g., 2*x + 3 = 7): 2*x + 3 = 7
✅ Solution: x = 2.0

Enter an equation (e.g., 2*x + 3 = 7): 3*x - 5 = 10
✅ Solution: x = 5.0
```

### Supported Operations

- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Power: `**` or `^`
- Parentheses for grouping: `()`

### History File

All solved problems are automatically saved to `math_history.txt` in the following format:
```
[2025-10-22 14:51:44] Problem: (15 + 25) / 2 | Result: 20.0
[2025-10-22 14:51:44] Problem: 3*x - 5 = 10 | Result: x = 5.0
[2025-10-22 14:51:44] Problem: 2**10 | Result: 1024.0
```
