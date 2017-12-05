increment_strategies = [
    lambda v: v + 1,
    lambda v: v - 1 if v >= 3 else v + 1
]

for f in increment_strategies:
    with open("05_input.txt") as file:
        program = list(map(int, file))

    pc = 0
    steps = 0
    while 0 <= pc < len(program):
        offset = program[pc]
        program[pc] = f(program[pc])
        pc += offset
        steps += 1

    print(steps)
