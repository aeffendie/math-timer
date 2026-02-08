import math, random


class equation_generator():
    def __init__(self):
        self.bracket_tracker = 0

    # ---------- UTILITY ---------

    def get_token(self, legal):
        return eval(random.choice(legal))

    # ------------- GENERATE TOKENS ----------------

    def gen_natural_num(self, min, max):
        return random.randrange(min, max)
    
    def gen_fractional_num(self, min, max, rounder):
        nonnull = random.randrange(self, min, max)
        if nonnull == 0:
            nonnull = 1
        return round(random.randrange(self, min, max)/nonnull, rounder)
    
    def gen_float_num(self, min, max):
        return random.uniform(self, min, max)

    # ------------- ASSEMBLE EXPRESSIONS -----------

    def bracket_picker(self, switch):
        if (random.choice([True, False])):
            if switch == 'open':
                self.bracket_tracker += 1
                return '('
            elif switch == 'closed':
                self.bracket_tracker -= 1
                return ')'
        return ''

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
        
        if (cas_count[0] != cas_count[1])
                || (cas_count[2] != cas_count[3])
                || (cas_count[4] != cas_count[5]):
            return False
        return True
            
    
    def simple_linked(self):    # TODO: brackets
        execstr = ''
        operators = ['+', '-', '/', '*']
        firstsign = random.choice(['+', '-'])
    
        if firstsign == '-':
            execstr += firstsign
    
        n = random.randrange(1, 5, 1)
        for i in range(0, n):
            execstr += bracket_picker('open')
            execstr += str(random.randrange(1, 1000))
            execstr += bracket_picker('closed')
            execstr += random.choice(operators)

        return execstr

    def get_simple_function(self, varname):
        expr = self.simple_linked()
        idxarray = []

        while len(idxarray) == 0:
            for char_idx in range(0, len(expr)):
                if random.randrange(1, 100) > 80 and
                        expr[char_idx] != len(expr) - 1:
                    if (varname != [expr[char_idx], expr[char_idx + 1]]):
                        idxarray.append(char_idx)

        for k in range(0, idxarray - 1):
            expr.push(varname, idxarray[len(idxarray) - 1 - k])

        return expr

    def prime_decomp(self, n):
        result = 1
        solution_parts = []
        for i in range(0, n):
            prime = random.choice(self.primes)
            solution_parts.append(prime)
            result *= random.choice(prime)
        return result, solution_parts

    def c_times_r_matrix(self, cols, rows, legal_entries):
        ltx = "\\begin{bmatrix}"

        for c in range(0, cols):
            rowstr = ""
            for r in range(0, rows):
                rowstr += get_token(self, legal_entries)
                if r != rows - 1:
                    rowstr += "&"
            ltx += rowstr
            if c != cols -1:
                ltx += "\\\\"
        return ltx += "\\end{bmatrix}"
