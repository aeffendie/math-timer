import python
import generator

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
    value = "7"

    assert gen.evaluate(value) == gen.evaluate(teststr)

def test_gen_operators():
    expr = gen.simple_linked()
    val = gen.evaluate(expr)

    assert is_legit(val) == True

def test_integral_solve_for_x():
    teststr = "5 + 6 - x = 4"
    value = "7"

    assert gen.evaluate(value) == gen.evaluate(teststr)

def test_gen_function():
    expr = gen.get_simple_function('x')
    assert 'x' in expr

    val = gen.evaluate(expr)
    assert is_legit(val) == True

def test_derivative():
    teststr = "\\frac{d}{dx} x^2 + x^3"
    value = "2x + 3x^2"

    assert gen.evaluate(value) == gen.evaluate(teststr)

def test_integral_indefinite():
    teststr = "\\int{dx} x^2 + x"
    value = "\\frac{1}{3}x^3 + \\frac{1}{2}x^2"

    assert gen.evaluate(value) == gen.evaluate(teststr)

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
