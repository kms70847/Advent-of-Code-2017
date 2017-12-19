with open("19_input.txt") as file:
    data = file.read().split("\n")

height = len(data)
width = len(data[0])

for i in range(width):
    if data[0][i] != " ":
        pos = i+0j
        break

heading = 0+1j
letters = []
steps = 0
while True:
    steps += 1
    pos += heading
    x,y = int(pos.real), int(pos.imag)
    cur = data[y][x]
    if not cur.strip():
        break
    elif cur.isalpha():
        letters.append(cur)
    elif cur == "+":
        candidate_headings = (heading * 1j, heading * 1j**3)
        for candidate in candidate_headings:
            next = pos + candidate
            x, y = int(next.real), int(next.imag)
            if 0 <= x < width and 0 <= y < height and data[y][x].strip():
                heading = candidate
                break
print("".join(letters))
print(steps)
