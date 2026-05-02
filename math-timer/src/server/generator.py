import math, random
from sympy.parsing.latex import parse_latex


class equation_generator():
    def __init__(self):
        self.bracket_tracker = 0
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 
                47, 51, 53, 61, 67, 71]

    # ---------- UTILITY ---------

    def get_token(self, legal):
        return eval(random.choice(legal))

    def evaluate(self, value):
        as_symbol = parse_latex(value)
        return as_symbol.evalf().doit()

    # ------------- GENERATE TOKENS ----------------

    def gen_natural_num(self, min, max):
        return str(random.randrange(min, max))
    
    def gen_fractional_num(self, min, max, rounder):
        nonnull = random.randrange(min, max)
        if nonnull == 0:
            nonnull = 1
        return str(round(random.randrange(min, max)/nonnull, rounder))
    
    def gen_float_num(self, min, max, rounder):
        return str(round(random.uniform(min, max), rounder))

    # ------------- ASSEMBLE EXPRESSIONS -----------

    def bracket_picker(self, switch):
        if (random.choice([True, False, False, False])):
            if switch == 'open':
                self.bracket_tracker += 1
                return '('
            elif switch == 'closed' and self.bracket_tracker > 0:
                self.bracket_tracker -= 1
                return ')'
        return ''

    def bracket_completer(self, expr):
        while (self.bracket_tracker != 0):
            self.bracket_tracker -= 1
            expr += ')'
        return expr

    def function_assembler(self, function_array):
        retstr = ''
        for i in function_array:
            retstr += i
        return retstr

    def brackets_check(self, f_arr):
        cas_count = [0, 0, 0, 0, 0, 0]
        bracket_types = ['(', ')', '[', ']', '{', '}']
        if i in f_arr:
            if i in bracket_types:
                cas_count[bracket_types.getIndex(i)] += 1
        
        if (cas_count[0] != cas_count[1]) or (cas_count[2] != cas_count[3]) or (cas_count[4] != cas_count[5]):
            return False
        return True
            
    def token_assemble(self, tokenlist):
        execstr = ''
        for t in tokenlist:
            execstr += t
        return execstr
    
    def simple_linked(self):
        tokens = [
            'self.gen_natural_num(0, 1000)', 
            'self.gen_fractional_num(0, 1000, 4)', 
            'self.gen_float_num(0, 1000, 4)'
        ]
        operators = ['+', '-', '/', '*']
        firstsign = random.choice(['+', '-'])
        constituents = []
    
        if firstsign == '-':
            execstr += firstsign
    
        n = random.randrange(1, 10, 1)
        for i in range(0, n):
            constituents.append(self.bracket_picker('open'))
            constituents.append(self.get_token(tokens))
            constituents.append(self.bracket_picker('closed'))
            constituents.append(random.choice(operators))

        constituents.append(self.get_token(tokens))
        constituents.append(self.bracket_completer(execstr))

        return constituents

    def get_simple_function(self, varname):
        expr = self.simple_linked()
        operators = ['+', '-', '/', '*']
        idxarray = []

        while len(idxarray) == 0:
            for char_idx in range(0, len(expr) - 1):
                if random.randrange(1, 100) > 80 and expr[char_idx] != len(expr) - 1:
                    if (varname != [expr[char_idx], expr[char_idx + 1]]):
                        idxarray.append(char_idx)
    
        if (expr[-1] in operators):
            expr += varname

        for k in range(0, len(idxarray) - 1):
            expr = expr[:len(idxarray) - 1 - k] + varname + expr[len(idxarray) - 1 - k:]

        if 'x' not in expr:
            expr += ' = x'
        else:
            expr += ' = 0'

        return expr

    def prime_decomp(self, n):
        result = 1
        solution_parts = []
        for i in range(0, n):
            prime = random.choice(self.primes)
            solution_parts.append(prime)
            result *= prime
        return result, solution_parts

    def c_times_r_matrix(self, cols, rows, legal_entries):
        ltx = "\\begin{bmatrix}"

        for c in range(0, cols):
            rowstr = ""
            for r in range(0, rows):
                rowstr += self.get_token(legal_entries)
                if r != rows - 1:
                    rowstr += " & "
            ltx += rowstr
            if c != cols -1:
                ltx += "\\\\"
        return ltx + "\\end{bmatrix}"
