with open("04_input.txt") as file:
    data = [line.split() for line in file if line.strip()]

#part 1
total = sum(1 for row in data if len(row) == len(set(row)))
print(total)

#part 2
total = sum(1 for row in data if len(row) == len(set("".join(sorted(word)) for word in row)))
print(total)
