def parse(iterable_of_strings):
    return [list(map(int, line.split())) for line in iterable_of_strings]

def checksum(data):
    return sum(max(row) - min(row) for row in data)

def iter_distinct_pairs(seq):
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            yield seq[i], seq[j]
            yield seq[j], seq[i]

with open("02_input.txt") as file:
    data = parse(file)

#part 1
print(checksum(data))

#part 2
print(sum(
    next(
        int(a/b) for a,b in iter_distinct_pairs(row) if a%b == 0
    )
    for row in data
))
