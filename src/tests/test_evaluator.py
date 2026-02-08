import sys, os
from sympy import solve
from ..server import generator

gen = generator.equation_generator()

def is_legit(val):
    success = False

    try:
        if float(val) != None:
            success = True
    except:
        pass
    return success

def test_operators():
    teststr = "(\\frac{4}{2} - 3) * (5 + 4/2)"
    value = "-7"

    assert gen.evaluate(value) == gen.evaluate(teststr)

def test_gen_operators():
    expr = gen.simple_linked()
    print(expr)
    val = gen.evaluate(expr)

    assert is_legit(val) == True

def test_solve_for_x():
    teststr = "5 + 6 - x = 4"
    value = "7"

    assert gen.evaluate(value) == solve(gen.evaluate(teststr), 'x')[0]

def test_gen_function():
    expr = gen.get_simple_function('x')
    assert 'x' in expr

    val = solve(gen.evaluate(expr), 'x')[0]
    assert is_legit(val) == True

def test_derivative():
    teststr = "\\frac{d}{dx} (x^2 + x^3)"
    value = "2.0x + 3.0x^2"

    assert gen.evaluate(value + '-' + teststr)  == 0

def test_integral_indefinite():
    teststr = r"\int{dx} x^2 + x"
    value = r"\frac{1}{3}x^3 + \frac{1}{2}x^2"

    assert gen.evaluate(value +'-'+ teststr) < 0.1

def test_integral_definite():
    pass

def test_matrix_multi():
    pass

def test_matrix_multi():
    pass

def test_matrix_inversion():
    pass

# --------- Some specific integrals

# --------- Some differential equations

# -------- 
