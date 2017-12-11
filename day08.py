from collections import defaultdict
import operator as o

registers = defaultdict(int)

comparisons = {">=": o.ge, ">": o.gt, "<=": o.le, "<": o.lt, "==": o.eq, "!=": o.ne}

highest = 0

with open("08_input.txt") as file:
    for line in file:
        register, op, amt, _, l, cmp, r = line.split()
        if comparisons[cmp](registers[l], int(r)):
            registers[register] += int(amt) * (1 if op == "inc" else -1)
        highest = max(registers[register], highest)

print(max(registers.values()))
print(highest)
