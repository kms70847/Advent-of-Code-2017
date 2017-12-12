from collections import defaultdict

d = defaultdict(set)
with open("input") as file:
    for line in file:
        l, rs = line.strip().split(" <-> ")
        for r in rs.split(", "):
            d[l].add(r)
            d[r].add(l)

def flood_fill(start):
    to_visit = {start}
    seen = set()
    while to_visit:
        current = to_visit.pop()
        seen.add(current)
        for neighbor in d[current]:
            if neighbor not in seen:
                to_visit.add(neighbor)
    return seen

print(len(flood_fill("0")))

groups = 0
to_visit = set(d.keys())
while to_visit:
    start = to_visit.pop()
    to_visit -= flood_fill(start)
    groups += 1
print(groups)
