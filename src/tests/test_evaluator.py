import sys, os
# import numpy as np
from sympy import solve
from ..server import generator

gen = generator.equation_generator()

def is_legit(val):
    success = False

    try:
        #if not np.isnan(val):
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

def test_build_matrix():
    entries = [
            'self.gen_natural_num(-100, 100)',
            'self.gen_fractional_num(-100, 100, 2)',
            'self.gen_float_num(-100, 100, 2)',
    ]

    mat = gen.c_times_r_matrix(4, 4, entries)

def test_matrix_multi():
    pass

def test_matrix_multi():
    pass

def test_matrix_inversion():
    pass

# --------- Some specific integrals

# --------- Some differential equations

# -------- Some weird ones

def test_prime_decomp():
    product, primes = gen.prime_decomp(4)
    check_product = 1

    for p in primes:
        check_product *= p

    assert product == check_product
