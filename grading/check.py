import utils
import resource
import subprocess
from pycparser import c_ast

# 195 MiB of memory
BYTES = 195 * 1024 * 1024

# bit_ops
# C loop visitor
class LoopCondVisitor(c_ast.NodeVisitor):

    def __init__(self):
        self.found = False

    def visit_While(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_DoWhile(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_Goto(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_If(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_Switch(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_TernaryOp(self, node):
        self.found = True
        self.generic_visit(node)

    def visit_For(self, node):
        self.found = True
        self.generic_visit(node)

    def reset(self):
        self.found = False
# bit_ops

# checks bit ops
def check_bitops():
    try:
        # compile
        task = utils.make(target='bit_ops')
        if task.returncode != 0:
            return (0, utils.failed('compilation error'), task.stderr.decode().strip())
        # check loops
        v = LoopCondVisitor()
        # flip_bit
        v.visit(utils.find_func(utils.parse_c('ex1/flip_bit'), 'flip_bit'))
        if v.found:
            return (0, utils.failed('[flip_bit] don\'t use loops/conds please... ¯\\_(⊙︿⊙)_/¯'), '')
        # get_bit
        v.visit(utils.find_func(utils.parse_c('ex1/get_bit'), 'get_bit'))
        if v.found:
            return (0, utils.failed('[get_bit] don\'t use loops/conds please... ¯\\_(⊙︿⊙)_/¯'), '')
        # set_bit
        v.visit(utils.find_func(utils.parse_c('ex1/set_bit'), 'set_bit'))
        if v.found:
            return (0, utils.failed('[set_bit] don\'t use loops/conds please... ¯\\_(⊙︿⊙)_/¯'), '')
        # run tests
        task = utils.execute(cmd=['./bit_ops'], timeout=15)
        if task.returncode != 0:
            return (0, utils.failed('runtime error'), task.stderr.decode().strip())
        # Output
        output = task.stdout.decode().strip().split('\n')

        f = open('ex1.expected', 'r')
        expected = f.read().strip()
        expected = expected.split('\n')
        f.close()

        grade = 0
        wrong = 0
        for (exp, out) in zip(expected, output):
            exp = exp.strip()
            out = out.strip()
            if exp == out:
                grade += 35 / 19
            else:
                wrong += 1
        if wrong == 19:
            return (0, utils.failed('all tests failed...'), '')
        elif wrong == 15:
            return (0, utils.failed('you only got base cases right...'), '')
        elif wrong != 0:
            return (round(grade), utils.incomplete('some tests failed...'), '')
        else:
            return (40, utils.passed(), '')
    except subprocess.TimeoutExpired:
        return (0, utils.failed('TIMEOUT'), '')
    except Exception as e:
        print(e)
        return (0, utils.failed('memory limit exceeded'), '')


# checks lfsr calculate
def check_lfsr():
    try:
        # compile
        task = utils.make(target='lfsr')
        if task.returncode != 0:
            return (0, utils.failed('compilation error'), task.stderr.decode().strip())
        # check loops
        v = LoopCondVisitor()
        # flip_bit
        v.visit(utils.find_func(utils.parse_c('ex2/lfsr_calculate'), 'lfsr_calculate'))
        if v.found:
            return (0, utils.failed('don\'t use loops/conds please... ¯\\_(⊙︿⊙)_/¯'), '')
        # run tests
        task = utils.execute(cmd=['./lfsr'], timeout=5)
        if task.returncode != 0:
            return (0, utils.failed('runtime error'), task.stderr.decode().strip())
        # Output
        output = task.stdout.decode().strip()
        f = open('ex2.expected', 'r')
        expected = f.read().strip()
        f.close()
        for line1, line2 in zip(output.split('\n'), expected.split('\n')):
            line1 = line1.strip()
            line2 = line2.strip()
            if line1 != line2 and 'congratulations! it works!' in output.lower():
                return (0, utils.failed('Please use the correct indexes...'), '')
            if line1 != line2:
                return (0, utils.failed('LFSR not working correctly...'), '')
        return (30, utils.passed(), '')
    except subprocess.TimeoutExpired:
        return (0, utils.failed('TIMEOUT'), '')
    except Exception as e:
        print(e)
        return (0, utils.failed('memory limit exceeded'), '')


# checks concat_bits
def check_concatbits():
    try:
        # compile
        task = utils.make(target='concat_bits')
        if task.returncode != 0:
            return (0, utils.failed('compilation error'), task.stderr.decode().strip())
        # run tests
        task = utils.execute(cmd=['./concat_bits'], timeout=5)
        if task.returncode != 0:
            return (0, utils.failed('runtime error'), task.stderr.decode().strip())
        if task.returncode != 0:
            return (0, utils.failed('runtime error'), task.stderr.decode().strip())
        
        # Output
        output = task.stdout.decode().strip().split('\n')

        f = open('ex3.expected', 'r')
        expected = f.read().strip()
        expected = expected.split('\n')
        f.close()

        grade = 0
        wrong = 0
        for (exp, out) in zip(expected, output):
            exp = exp.strip()
            out = out.strip()
            if exp == out:
                grade += 35 / 6
            else:
                wrong += 1
        if wrong == 6:
            return (0, utils.failed('all tests failed...'), '')
        elif wrong != 0:
            return (round(grade), utils.incomplete('some tests failed...'), '')
        else:
            return (35, utils.passed(), '')
    except subprocess.TimeoutExpired:
        return (0, utils.failed('TIMEOUT'), '')
    except Exception as e:
        print(e)
        return (0, utils.failed('memory limit exceeded'), '')



def lab1_c():
    not_found = utils.expected_files(['./ex1/flip_bit.c', './ex1/flip_bit.c', './ex1/flip_bit.c', './ex2/lfsr_calculate.c', './ex3/concat_bits.c'])

    if len(not_found) == 0:
        table = []
        
        bitops = check_bitops()
        table.append(['1. bit_ops', bitops[0], bitops[1]])
        lfsr = check_lfsr()
        table.append(['2. lfsr', lfsr[0], lfsr[1]])
        concatbits = check_concatbits()
        table.append(['3. concat_bits', concatbits[0], concatbits[1]])
        
        grade = 0
        grade += bitops[0]
        grade += lfsr[0]
        grade += concatbits[0]

        errors = ''
        errors += '\n' + utils.create_error('bit_ops', bitops[2])
        errors += '\n' + utils.create_error('lfsr', lfsr[2])
        errors += '\n' + utils.create_error('concat_bits', concatbits[2])

        errors = errors.strip()
        grade = min(grade, 100)
        report = utils.report(table)
        print(report)
        if errors != '':
            report += '\n\nMore Info:\n\n' + errors
        return utils.write_result(grade, report)
    else:
        utils.write_result(0, 'missing files: %s' % (','.join(not_found)))


if __name__ == '__main__':
    resource.setrlimit(resource.RLIMIT_AS, (BYTES, BYTES))
    lab1_c()
    utils.fix_ownership()
