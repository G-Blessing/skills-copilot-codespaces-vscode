#!/usr/bin/env python3
"""
AI Math Helper - A beginner-friendly math assistant
Supports basic arithmetic and simple algebraic equations
"""

import sympy as sp
from datetime import datetime


def display_menu():
    """Display the main menu options"""
    print("\n" + "="*50)
    print("🤖 AI Math Helper - Your Friendly Math Assistant")
    print("="*50)
    print("1. Solve Arithmetic Expression")
    print("2. Solve Algebraic Equation (for x)")
    print("3. Exit")
    print("="*50)


def save_to_history(problem, result):
    """Save solved problems to math_history.txt"""
    try:
        with open('math_history.txt', 'a') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] Problem: {problem} | Result: {result}\n")
    except Exception as e:
        print(f"⚠️  Warning: Could not save to history - {e}")


def solve_arithmetic():
    """Solve basic arithmetic expressions"""
    print("\n📊 Arithmetic Expression Solver")
    print("-" * 50)
    expression = input("Enter an arithmetic expression (e.g., 3 + 5 * 2): ").strip()
    
    if not expression:
        print("❌ Error: Expression cannot be empty!")
        return
    
    try:
        # Use sympy to safely evaluate the expression
        result = sp.sympify(expression)
        result_value = float(result.evalf())
        
        print(f"✅ Result: {expression} = {result_value}")
        save_to_history(expression, result_value)
        
    except Exception as e:
        print(f"❌ Error: Could not evaluate expression - {e}")
        print("💡 Tip: Make sure you use valid operators (+, -, *, /, ^, **)")


def solve_algebra():
    """Solve simple algebraic equations for x"""
    print("\n🔢 Algebraic Equation Solver")
    print("-" * 50)
    equation = input("Enter an equation (e.g., 2*x + 3 = 7): ").strip()
    
    if not equation:
        print("❌ Error: Equation cannot be empty!")
        return
    
    if '=' not in equation:
        print("❌ Error: Equation must contain an '=' sign!")
        return
    
    try:
        # Split equation into left and right sides
        left, right = equation.split('=')
        left = left.strip()
        right = right.strip()
        
        # Define the variable x
        x = sp.Symbol('x')
        
        # Parse both sides of the equation
        left_expr = sp.sympify(left)
        right_expr = sp.sympify(right)
        
        # Solve the equation
        equation_to_solve = sp.Eq(left_expr, right_expr)
        solutions = sp.solve(equation_to_solve, x)
        
        if not solutions:
            print("❌ No solution found for this equation!")
            return
        
        # Display the solution(s)
        if len(solutions) == 1:
            solution = float(solutions[0].evalf()) if solutions[0].is_number else solutions[0]
            print(f"✅ Solution: x = {solution}")
            save_to_history(equation, f"x = {solution}")
        else:
            solutions_str = ", ".join([str(float(sol.evalf()) if sol.is_number else sol) for sol in solutions])
            print(f"✅ Solutions: x = {solutions_str}")
            save_to_history(equation, f"x = {solutions_str}")
            
    except Exception as e:
        print(f"❌ Error: Could not solve equation - {e}")
        print("💡 Tip: Use 'x' as the variable and format like '2*x + 3 = 7'")


def main():
    """Main program loop"""
    print("\n" + "🎉" * 25)
    print("Welcome to AI Math Helper!")
    print("Your friendly assistant for solving math problems")
    print("🎉" * 25)
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                solve_arithmetic()
            elif choice == '2':
                solve_algebra()
            elif choice == '3':
                print("\n👋 Thank you for using AI Math Helper!")
                print("💾 Your solutions have been saved to 'math_history.txt'")
                print("Goodbye! 🌟\n")
                break
            else:
                print("❌ Invalid choice! Please enter 1, 2, or 3.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted. Goodbye! 🌟\n")
            break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
