
with open("23_input.txt") as file:
    program = file.read().strip().split("\n")

def execute(program, registers):
    def get(s):
        if s in registers:
            return registers[s]
        else:
            return int(s)

    pc = 0
    muls_invoked = 0
    while pc >= 0 and pc < len(program):
        op, *args = program[pc].split()
        if op == "set":
            registers[args[0]] = get(args[1])
        elif op == "sub":
            registers[args[0]] -= get(args[1])
        elif op == "mul":
            muls_invoked += 1
            registers[args[0]] *= get(args[1])
        elif op == "jnz":
            if get(args[0]) != 0:
                pc += get(args[1])
                continue
        pc += 1
    return muls_invoked

registers = {c:0 for c in "abcdefgh"}
print(execute(program, registers))

#part 2: looks like the code is trying to count all the composite numbers between 108400 and 125400, using a step of 17.
#see companion document for the deduction.

def is_prime(x):
    """can't be bothered to write a more efficient version."""
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print([(i, is_prime(i)) for i in range(2, 20)])

b = 108400
c = b + 17000
total = 0
for x in range(b,c+1,17):
    if not is_prime(x):
        total += 1
print(total)
