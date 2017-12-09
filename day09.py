with open("09_input.txt") as file:
    data = file.read()
idx = 0

def parse_group():
    global idx
    results = []
    idx += 1
    while data[idx] != "}":
        if data[idx] == "<":
            results.append(parse_junk())
        elif data[idx] == "{":
            results.append(parse_group())
        elif data[idx] == ",":
            idx += 1
    idx += 1
    return results

def parse_junk():
    global idx
    results = []
    while data[idx] != ">":
        if data[idx] == "!":
            idx += 1
        else:
            results.append(data[idx])
        idx += 1
    idx += 1
    return "".join(results) + ">"

def value(obj, depth=1):
    total = depth
    for child in obj:
        if isinstance(child, list):
            total += value(child, depth+1)
    return total

def walk(obj):
    yield obj
    for child in obj:
        if isinstance(child, str):
            yield child
        else:
            yield from walk(child)            

x = parse_group()
print(value(x))
print(sum(len(obj)-2 for obj in walk(x) if isinstance(obj, str)))
