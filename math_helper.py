#!/usr/bin/env python3
"""
AI Math Helper - A chatbot that solves basic math and logic problems.

This chatbot can:
- Solve arithmetic expressions
- Solve algebraic equations
- Simplify expressions
- Solve basic logic problems
"""

import re
import sympy as sp
from sympy import symbols, simplify, solve, expand, factor, diff, integrate
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application


class MathHelper:
    """AI Math Helper chatbot for solving math and logic problems."""
    
    def __init__(self):
        """Initialize the Math Helper."""
        self.transformations = (standard_transformations + 
                               (implicit_multiplication_application,))
        print("AI Math Helper initialized!")
        print("I can help you with:")
        print("  - Arithmetic calculations (e.g., '2 + 2', '5 * 3')")
        print("  - Algebraic equations (e.g., 'solve x^2 - 4 = 0')")
        print("  - Simplify expressions (e.g., 'simplify (x+1)^2')")
        print("  - Derivatives (e.g., 'derivative of x^2')")
        print("  - Integrals (e.g., 'integrate x^2')")
        print("  - Logic problems (e.g., 'if A then B, A is true, what is B?')")
        print()
    
    def solve_arithmetic(self, expression):
        """Solve basic arithmetic expressions."""
        try:
            # Replace ^ with ** for exponentiation
            expression = expression.replace('^', '**')
            # Parse and evaluate the expression
            result = parse_expr(expression, transformations=self.transformations)
            return f"Result: {result} = {float(result)}"
        except Exception as e:
            return f"Error evaluating arithmetic: {str(e)}"
    
    def solve_equation(self, equation_str):
        """Solve algebraic equations."""
        try:
            # Replace ^ with ** for exponentiation
            equation_str = equation_str.replace('^', '**')
            # Handle equations with '='
            if '=' in equation_str:
                left, right = equation_str.split('=')
                equation = parse_expr(left, transformations=self.transformations) - parse_expr(right, transformations=self.transformations)
            else:
                equation = parse_expr(equation_str, transformations=self.transformations)
            
            # Find all symbols in the equation
            variables = list(equation.free_symbols)
            
            if not variables:
                return f"Result: {equation} = {float(equation)}"
            
            # Solve the equation
            solutions = solve(equation, variables)
            
            if isinstance(solutions, dict):
                result = "Solutions:\n"
                for var, val in solutions.items():
                    result += f"  {var} = {val}\n"
                return result.strip()
            elif isinstance(solutions, list):
                if len(variables) == 1:
                    var = variables[0]
                    result = f"Solutions for {var}:\n"
                    for sol in solutions:
                        result += f"  {var} = {sol}\n"
                    return result.strip()
                else:
                    return f"Solutions: {solutions}"
            else:
                return f"Solution: {solutions}"
                
        except Exception as e:
            return f"Error solving equation: {str(e)}"
    
    def simplify_expression(self, expression_str):
        """Simplify mathematical expressions."""
        try:
            # Replace ^ with ** for exponentiation
            expression_str = expression_str.replace('^', '**')
            expr = parse_expr(expression_str, transformations=self.transformations)
            simplified = simplify(expr)
            expanded = expand(expr)
            factored = factor(expr)
            
            result = f"Original: {expr}\n"
            result += f"Simplified: {simplified}\n"
            
            if str(expanded) != str(expr):
                result += f"Expanded: {expanded}\n"
            
            if str(factored) != str(expr) and str(factored) != str(simplified):
                result += f"Factored: {factored}"
            
            return result.strip()
        except Exception as e:
            return f"Error simplifying expression: {str(e)}"
    
    def calculate_derivative(self, expression_str, variable='x'):
        """Calculate the derivative of an expression."""
        try:
            # Replace ^ with ** for exponentiation
            expression_str = expression_str.replace('^', '**')
            expr = parse_expr(expression_str, transformations=self.transformations)
            var = symbols(variable)
            
            if var not in expr.free_symbols:
                # Try to find the variable in the expression
                free_vars = list(expr.free_symbols)
                if free_vars:
                    var = free_vars[0]
                else:
                    return f"No variable found in expression: {expr}"
            
            derivative = diff(expr, var)
            return f"Derivative of {expr} with respect to {var}:\n  d/d{var} = {derivative}"
        except Exception as e:
            return f"Error calculating derivative: {str(e)}"
    
    def calculate_integral(self, expression_str, variable='x'):
        """Calculate the integral of an expression."""
        try:
            # Replace ^ with ** for exponentiation
            expression_str = expression_str.replace('^', '**')
            expr = parse_expr(expression_str, transformations=self.transformations)
            var = symbols(variable)
            
            if var not in expr.free_symbols:
                # Try to find the variable in the expression
                free_vars = list(expr.free_symbols)
                if free_vars:
                    var = free_vars[0]
                else:
                    return f"No variable found in expression: {expr}"
            
            integral = integrate(expr, var)
            return f"Integral of {expr} with respect to {var}:\n  ∫ {expr} d{var} = {integral} + C"
        except Exception as e:
            return f"Error calculating integral: {str(e)}"
    
    def solve_logic_problem(self, problem):
        """Solve basic logic problems using rule-based reasoning."""
        problem_lower = problem.lower()
        
        # Pattern: "if A then B, A is true"
        if_then_pattern = r'if\s+(.+?)\s+then\s+(.+?)(?:,|\.)\s*(.+?)\s+is\s+(true|false)'
        match = re.search(if_then_pattern, problem_lower)
        
        if match:
            antecedent = match.group(1).strip()
            consequent = match.group(2).strip()
            given_statement = match.group(3).strip()
            given_value = match.group(4).strip() == 'true'
            
            result = f"Logic Analysis:\n"
            result += f"  Rule: If {antecedent} then {consequent}\n"
            result += f"  Given: {given_statement} is {given_value}\n"
            
            if given_statement == antecedent or given_statement in antecedent:
                if given_value:
                    result += f"  Conclusion: {consequent} is TRUE (Modus Ponens)"
                else:
                    result += f"  Conclusion: Cannot determine {consequent} (no rule for false antecedent)"
            elif given_statement == consequent or given_statement in consequent:
                if not given_value:
                    result += f"  Conclusion: {antecedent} is FALSE (Modus Tollens)"
                else:
                    result += f"  Conclusion: Cannot determine {antecedent} (affirming the consequent)"
            else:
                result += f"  Conclusion: Cannot determine - given statement doesn't match rule"
            
            return result
        
        # Pattern: "A and B"
        and_pattern = r'(.+?)\s+and\s+(.+?)\s+are\s+(true|false|both true|both false)'
        match = re.search(and_pattern, problem_lower)
        
        if match:
            a = match.group(1).strip()
            b = match.group(2).strip()
            value = match.group(3).strip()
            
            result = f"Logic Analysis:\n"
            if 'both true' in value or value == 'true':
                result += f"  {a} AND {b} = TRUE\n"
                result += f"  Therefore: {a} is TRUE, {b} is TRUE"
            elif 'both false' in value or value == 'false':
                result += f"  {a} AND {b} = FALSE\n"
                result += f"  Therefore: At least one of {a} or {b} is FALSE"
            
            return result
        
        # Pattern: "A or B"
        or_pattern = r'(.+?)\s+or\s+(.+?)\s+is\s+(true|false)'
        match = re.search(or_pattern, problem_lower)
        
        if match:
            a = match.group(1).strip()
            b = match.group(2).strip()
            value = match.group(3).strip() == 'true'
            
            result = f"Logic Analysis:\n"
            if value:
                result += f"  {a} OR {b} = TRUE\n"
                result += f"  Therefore: At least one of {a} or {b} is TRUE"
            else:
                result += f"  {a} OR {b} = FALSE\n"
                result += f"  Therefore: {a} is FALSE, {b} is FALSE"
            
            return result
        
        return "I couldn't recognize the logic problem format. Try patterns like:\n" \
               "  - 'If A then B, A is true'\n" \
               "  - 'A and B are both true'\n" \
               "  - 'A or B is true'"
    
    def process_query(self, query):
        """Process a user query and determine the appropriate action."""
        query_lower = query.lower().strip()
        
        # Check for exit commands
        if query_lower in ['quit', 'exit', 'bye', 'goodbye']:
            return None
        
        # Check for help
        if query_lower in ['help', '?']:
            return self.__init__.__doc__
        
        # Check for derivative
        if 'derivative' in query_lower or 'diff' in query_lower:
            # Extract expression after "of"
            if ' of ' in query_lower:
                expr = query.split(' of ', 1)[1].strip()
                return self.calculate_derivative(expr)
            else:
                return "Please specify the expression (e.g., 'derivative of x^2')"
        
        # Check for integral
        if 'integral' in query_lower or 'integrate' in query_lower:
            # Extract expression after "of" or command
            if ' of ' in query_lower:
                expr = query.split(' of ', 1)[1].strip()
            else:
                expr = query.replace('integrate', '').replace('integral', '').strip()
            
            if expr:
                return self.calculate_integral(expr)
            else:
                return "Please specify the expression (e.g., 'integrate x^2')"
        
        # Check for simplify
        if 'simplify' in query_lower:
            expr = query.lower().replace('simplify', '').strip()
            if expr:
                return self.simplify_expression(expr)
            else:
                return "Please provide an expression to simplify"
        
        # Check for solve
        if 'solve' in query_lower:
            equation = query.lower().replace('solve', '').strip()
            if equation:
                return self.solve_equation(equation)
            else:
                return "Please provide an equation to solve"
        
        # Try to detect if it's an equation (contains '=')
        if '=' in query:
            return self.solve_equation(query)
        
        # Check for logic problems (contains logical keywords) - only if no math keywords
        if any(keyword in query_lower for keyword in ['if', 'then']) or \
           (any(keyword in query_lower for keyword in ['and', 'or']) and any(word in query_lower for word in ['true', 'false'])):
            return self.solve_logic_problem(query)
        
        # Otherwise, treat as arithmetic or algebraic expression
        try:
            # Replace ^ with ** for exponentiation before parsing
            query_normalized = query.replace('^', '**')
            # First try to parse it
            expr = parse_expr(query_normalized, transformations=self.transformations)
            
            # If it has variables, simplify it
            if expr.free_symbols:
                return self.simplify_expression(query)
            else:
                # It's just arithmetic
                return self.solve_arithmetic(query)
        except:
            return "I couldn't understand your query. Type 'help' for examples of what I can do."
    
    def run(self):
        """Run the interactive chatbot."""
        print("AI Math Helper is ready! Type 'help' for examples or 'quit' to exit.\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                response = self.process_query(user_input)
                
                if response is None:
                    print("\nGoodbye! Thanks for using AI Math Helper!")
                    break
                
                print(f"\nAI: {response}\n")
                
            except KeyboardInterrupt:
                print("\n\nGoodbye! Thanks for using AI Math Helper!")
                break
            except Exception as e:
                print(f"\nError: {str(e)}\n")


def main():
    """Main entry point for the AI Math Helper."""
    helper = MathHelper()
    helper.run()


if __name__ == "__main__":
    main()
