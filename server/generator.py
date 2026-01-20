import math, random


class equation_generator():
    def __init__(self):
        self.bracket_tracker = 0

    def bracket_picker(self, switch):
        if (random.choice([True, False])):
            if switch == 'open':
                self.bracket_tracker += 1
                return '('
            elif switch == 'closed':
                self.bracket_tracker -= 1
                return ')'
        return ''
            
    
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
