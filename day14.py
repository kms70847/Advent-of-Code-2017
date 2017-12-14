import functools

with open("14_input.txt") as file:
    INPUT = file.read().strip()

def hash_round(seq, lengths, idx=0, skip_size=0):
    seq = seq[:]
    for length in lengths:
        vals = [seq[(idx+i)%len(seq)] for i in range(length)][::-1]
        for i, val in enumerate(vals):
            seq[(idx+i)%len(seq)] = val
        idx = (idx + length + skip_size) % len(seq)
        skip_size += 1
    return seq, idx, skip_size

def knot_hash(message):
    seq = list(range(256))
    lengths = [ord(c) for c in message] + [17, 31, 73, 47, 23]
    idx = 0
    skip_size = 0
    for i in range(64):
        seq, idx, skip_size = hash_round(seq, lengths, idx, skip_size)
    blocks = [seq[i:i+16] for i in range(0, len(seq), 16)]
    multi_xor = lambda seq: functools.reduce(lambda a,b: a^b, seq, 0)
    dense_hash = list(map(multi_xor, blocks))
    result = "".join("{:0>2x}".format(x) for x in dense_hash)
    return result

def generate_grid(seed):
    data = []
    for i in range(128):
        s = knot_hash("{}-{}".format(seed, i))
        row = [int(c,16) >> n & 1 for c in s for n in range(3, -1, -1)]
        data.append(row)
    return data

def flood_fill(start, neighbor_func):
    to_visit = {start}
    seen = set()
    while to_visit:
        #print(to_visit, seen)
        current = to_visit.pop()
        seen.add(current)
        for neighbor in neighbor_func(current):
            if neighbor not in seen:
                to_visit.add(neighbor)
    return seen

def living_neighbors(pos):
    results = []
    x,y = pos
    deltas = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in deltas:
        if 0 <= x+dx < 128 and 0 <= y+dy < 128 and data[y+dy][x+dx]:
            results.append((x+dx, y+dy))
    return results

data = generate_grid(INPUT)

print(sum(sum(row) for row in data))

groups = 0
seen = set()
for j, row in enumerate(data):
    for i, cell in enumerate(row):
        if cell and (i,j) not in seen:
            seen |= flood_fill((i,j), living_neighbors)
            groups += 1

print(groups)
