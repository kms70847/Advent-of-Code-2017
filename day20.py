import re
import collections

"""
Currently too lazy to implement a proper solution that can resolve changes 
in distance ranking and/or collisions at arbitrarily large points in the future.
So we'll just run the simulation for 500 ticks and hope nothing interesting
happens after that.
"""
MAX_ROUNDS = 500

def magnitude(seq):
    return sum(map(abs, seq))

def get_data():
    data = []
    with open("20_input.txt") as file:
        for line in file:
            d = {}
            for part in line.split(", "):
                m = re.match(r"(.)=<(-?\d+),(-?\d+),(-?\d+)>", part)
                key, *vals = m.groups()
                d[key] = list(map(int,vals))
            data.append(d)
    return data

def tick(data):
    for d in data:
        for i in range(3):
            d["v"][i] += d["a"][i]
            d["p"][i] += d["v"][i]

def remove_collisions(data):
    positions = collections.defaultdict(list)
    for particle in data:
        positions[tuple(particle["p"])].append(particle)
    data[:] = [particle for v in positions.values() for particle in v if len(v) == 1]

#part 1
data = get_data()
for round in range(MAX_ROUNDS):
    tick(data)
closest = min(data, key=lambda d: magnitude(d["p"]))
print(data.index(closest))

#part 2
data = get_data()
for round in range(MAX_ROUNDS):
    remove_collisions(data)
    tick(data)
print(len(data))
