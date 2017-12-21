def transpose(data):
    return "\n".join("".join(row) for row in zip(*data.split("\n")))

def x_mirror(data):
    return "\n".join("".join(reversed(row)) for row in data.split("\n"))

def rotate_clockwise(data):
    return x_mirror(transpose(data))

def iter_variations(data):
    funcs = [transpose, x_mirror] * 4
    for f in funcs:
        yield data
        data = f(data)

def y_combine(groups):
    return "\n".join(groups)

def x_combine(groups):
    return transpose(y_combine(map(transpose, groups)))

def separate(data, chunk_size):
    rows = data.split("\n")
    size = len(rows)
    return [["\n".join("".join(rows[y+j][x+i] for i in range(chunk_size)) for j in range(chunk_size)) for x in range(0, size, chunk_size)] for y in range(0, size, chunk_size)]

def combine(separated_data):
    rows = [x_combine(row) for row in separated_data]
    return y_combine(rows)

d = {}
with open("21_input.txt") as file:
    for line in file:
        l,r = line.strip().replace("/", "\n").split(" => ")
        for x in iter_variations(l):
            d[x] = r

data = """.#.
..#
###"""

size = 3

for i in range(18):
    if i == 5: print(data.count("#"))
    if size % 2 == 0:
        blocks = separate(data, 2)
        size = size * 3 // 2 
    else:
        blocks = separate(data, 3)
        size = size * 4 // 3
    blocks = [[d[block] for block in row] for row in blocks]
    data = combine(blocks)

print(data.count("#"))
