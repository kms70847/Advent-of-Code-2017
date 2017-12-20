import re
import collections
import itertools
import math
import operator

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

def intersection(a, b):
    """
    given particles a and b, 
    returns the first non-negative integer time that they will collide, 
    or None if they don't collide at a non-negative integer time.
    """

    def is_perfect_square(x):
        root = int(math.sqrt(x))
        return root**2 == x

    def quadratic_for_ints(a,b,c):
        """returns a list of integer solutions"""
        if a == 0:
            if b == 0:
                if c == 0:
                    #nasty hack: there are infinite solutions,
                    #but we can't return an infinite list,
                    #so just return this sentinel value.
                    return [float("inf")]
                else:
                    return []
            else:
                if c%b != 0: return []
                return [-c//b]
        x = b**2 - 4*a*c
        if x < 0 or not is_perfect_square(x):
            return []
        ops = (operator.add, operator.sub)
        numerators = [op(-b, int(math.sqrt(x))) for op in ops]
        integer_results = [x // (2*a) for x in numerators if x % (2*a) == 0]
        return [x for x in integer_results if x>=0]

    if a == b:
        return 0

    candidates = []
    for i in range(3):
        da = b["a"][i]-a["a"][i]
        dv = b["v"][i]-a["v"][i]
        dp = b["p"][i]-a["p"][i]
        times = quadratic_for_ints(
            da,
            da + 2*dv,
            2*dp
        )
        if float("inf") not in times:
            candidates.append(set(times))
    candidates = set.intersection(*candidates)
    candidates = [t for t in candidates if t > 0]
    return min(candidates) if candidates else None

#part 1
#todo: find solution for this that doesn't assume the answer can be found within MAX_ROUNDS ticks
data = get_data()
for round in range(MAX_ROUNDS):
    tick(data)
closest = min(data, key=lambda d: magnitude(d["p"]))
print(data.index(closest))

#part 2
data = get_data()
#find all potential collisions, keyed by time
collisions = collections.defaultdict(set)
for i in range(len(data)):
    for j in range(i+1, len(data)):
        t = intersection(data[i],data[j])
        if t:
            collisions[t].add(i)
            collisions[t].add(j)

#not all of those possible collisions are necessarily real;
#if particles 0 and 1 collide at time T=23,
#then a projected collision of particles 0 and 2 at time T=42 won't occur.
#so let's iterate through these in time order and track which ones actually happen.
destroyed = set()
for k, v in sorted(collisions.items()):
    undestroyed_particles = [idx for idx in v if idx not in destroyed]
    if len(undestroyed_particles) >= 2:
        destroyed.update(set(v))
print(len(data) - len(destroyed))
