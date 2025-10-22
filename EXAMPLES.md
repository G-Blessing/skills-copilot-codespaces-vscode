# AI Math Helper - Examples

This document shows examples of the AI Math Helper chatbot in action.

## Feature Demonstrations

### 1. Arithmetic Operations
```
You: 2 + 2
AI: Result: 4 = 4.0

You: 2^10
AI: Result: 1024 = 1024.0

You: 10 / 2
AI: Result: 5 = 5.0
```

### 2. Solving Equations
```
You: solve x^2 - 4 = 0
AI: Solutions for x:
  x = -2
  x = 2

You: solve x^2 + 5*x + 6 = 0
AI: Solutions for x:
  x = -3
  x = -2

You: solve 2*x + 5 = 15
AI: Solutions for x:
  x = 5
```

### 3. Expression Simplification
```
You: simplify (x+1)^2
AI: Original: (x + 1)**2
Simplified: (x + 1)**2
Expanded: x**2 + 2*x + 1

You: simplify x^2 - 1
AI: Original: x**2 - 1
Simplified: x**2 - 1
Factored: (x - 1)*(x + 1)

You: simplify (x+2)*(x+3)
AI: Original: (x + 2)*(x + 3)
Simplified: (x + 2)*(x + 3)
Expanded: x**2 + 5*x + 6
```

### 4. Calculus - Derivatives
```
You: derivative of x^2
AI: Derivative of x**2 with respect to x:
  d/dx = 2*x

You: derivative of x^3 + 2*x^2
AI: Derivative of x**3 + 2*x**2 with respect to x:
  d/dx = 3*x**2 + 4*x

You: derivative of 2*x^3 + 3*x
AI: Derivative of 2*x**3 + 3*x with respect to x:
  d/dx = 6*x**2 + 3
```

### 5. Calculus - Integrals
```
You: integrate x^2
AI: Integral of x**2 with respect to x:
  ∫ x**2 dx = x**3/3 + C

You: integrate 2*x
AI: Integral of 2*x with respect to x:
  ∫ 2*x dx = x**2 + C

You: integrate sin(x)
AI: Integral of sin(x) with respect to x:
  ∫ sin(x) dx = -cos(x) + C
```

### 6. Logic Problems
```
You: if A then B, A is true
AI: Logic Analysis:
  Rule: If a then b
  Given: a is True
  Conclusion: b is TRUE (Modus Ponens)

You: if it is sunny then I go to beach, it is sunny is true
AI: Logic Analysis:
  Rule: If it is sunny then i go to beach
  Given: it is sunny is True
  Conclusion: i go to beach is TRUE (Modus Ponens)

You: P and Q are both true
AI: Logic Analysis:
  p AND q = TRUE
  Therefore: p is TRUE, q is TRUE

You: A or B is false
AI: Logic Analysis:
  a OR b = FALSE
  Therefore: a is FALSE, b is FALSE
```

## Running the Examples

To try these examples yourself:

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the chatbot:
```bash
python3 math_helper.py
```

3. Type any of the example queries above or create your own!

## Help Command

Type `help` to see all available features:
```
You: help
AI: Initialize the Math Helper.
```

## Exit

Type `quit`, `exit`, `bye`, or `goodbye` to exit the chatbot.
