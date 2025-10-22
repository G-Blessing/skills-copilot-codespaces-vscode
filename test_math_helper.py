#!/usr/bin/env python3
"""
Test script for AI Math Helper chatbot.
Tests various math and logic problems to verify functionality.
"""

from math_helper import MathHelper


def test_math_helper():
    """Test the Math Helper with various queries."""
    helper = MathHelper()
    
    test_cases = [
        # Arithmetic tests
        ("2 + 2", "arithmetic"),
        ("5 * 3", "arithmetic"),
        ("10 / 2", "arithmetic"),
        ("2^3", "arithmetic"),
        
        # Equation solving tests
        ("solve x^2 - 4 = 0", "equation"),
        ("solve 2*x + 5 = 15", "equation"),
        ("x^2 + 2*x + 1 = 0", "equation"),
        
        # Simplification tests
        ("simplify (x+1)^2", "simplify"),
        ("simplify x^2 - 1", "simplify"),
        
        # Derivative tests
        ("derivative of x^2", "derivative"),
        ("derivative of 2*x^3 + 3*x", "derivative"),
        
        # Integral tests
        ("integrate x^2", "integral"),
        ("integrate 2*x", "integral"),
        
        # Logic tests
        ("if A then B, A is true, what is B?", "logic"),
        ("if it rains then ground is wet, it rains is true", "logic"),
        ("P and Q are both true", "logic"),
        ("A or B is false", "logic"),
    ]
    
    print("\n" + "="*70)
    print("TESTING AI MATH HELPER")
    print("="*70 + "\n")
    
    passed = 0
    failed = 0
    
    for query, test_type in test_cases:
        print(f"\nTest ({test_type}): {query}")
        print("-" * 70)
        
        try:
            result = helper.process_query(query)
            
            if result and "Error" not in result and "couldn't" not in result:
                print(f"✓ PASSED")
                print(f"Response: {result[:200]}...")  # Show first 200 chars
                passed += 1
            else:
                print(f"✗ FAILED")
                print(f"Response: {result}")
                failed += 1
                
        except Exception as e:
            print(f"✗ FAILED with exception: {str(e)}")
            failed += 1
    
    print("\n" + "="*70)
    print(f"TEST SUMMARY: {passed} passed, {failed} failed out of {passed + failed} tests")
    print("="*70 + "\n")
    
    return passed, failed


if __name__ == "__main__":
    passed, failed = test_math_helper()
    
    # Exit with appropriate code
    exit(0 if failed == 0 else 1)
