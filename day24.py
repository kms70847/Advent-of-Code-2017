from collections import Counter, defaultdict

data = []
with open("24_input.txt") as file:
    for line in file:
        data.append(tuple(map(int, line.split("/"))))

assert len(data) == len(set(data))
d = defaultdict(set)
for component in data:
    for i in range(2):
        d[component[i]].add(component)

def strongest(base=0, seen=None):
    if seen is None: seen = set()
    strengths = []
    for candidate in d[base] - seen:
        next_base = sum(candidate) - base
        strengths.append(sum(candidate) + strongest(next_base, seen|{candidate}))
    if not strengths:
        return 0
    return max(strengths)

def longest(base=0, seen=None):
    if seen is None: seen = set()
    lengths_and_strengths = []
    for candidate in d[base] - seen:
        next_base = sum(candidate) - base
        next_length, next_strength = longest(next_base, seen | {candidate})
        lengths_and_strengths.append((
            strongest(next_base, seen|{candidate}) + 1,
            sum(candidate) + next_strength,
        ))
    if not lengths_and_strengths:
        return (0, 0)
    return max(lengths_and_strengths)

print(strongest())
print(longest()[1])
