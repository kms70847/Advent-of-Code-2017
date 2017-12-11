def distance_from_origin(pos):
    x,y = pos.real, pos.imag
    return int(min(
        abs(x) + abs(y),
        abs(x+y) + abs(x),
        abs(x+y) + abs(y),
    ))

with open("11_input.txt") as file:
    data = file.read().strip().split(",")

deltas = {"n": 0+1j, "s": 0-1j, "ne": 1+0j, "sw": -1+0j, "nw": -1+1j, "se": 1-1j}
positions = [0+0j]
for direction in data:
    positions.append(positions[-1]+deltas[direction])

print(distance_from_origin(positions[-1]))
print(max(distance_from_origin(pos) for pos in positions))
