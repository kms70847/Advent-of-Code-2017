import re
from types import SimpleNamespace
from collections import defaultdict

def odd_one_out(seq, key):
    d = defaultdict(list)
    for item in seq:
        d[key(item)].append(item)
    if len(d) != 2:
        raise Exception("Expected exactly two categories, got {}".format(len(d)))
    candidates = [item for bucket in d.values() for item in bucket if len(bucket) == 1]
    if len(candidates) != 1:
        raise Exception("Expected exactly one odd item out, got {}".format(len(candidates)))
    return candidates[0]

def all_equal(seq):
    return all(item == seq[0] for item in seq[1:])

def cumulative_weight(node):
    return node.weight + sum(cumulative_weight(child) for child in node.children)

data = defaultdict(SimpleNamespace)
with open("07_input.txt") as file:
    for line in file:
        name, raw_weight, raw_children = re.match(r"(\w+) \((\d+)\)(?: -> )?(.*)$", line).groups()
        data[name].name = name
        data[name].parent = None
        data[name].weight = int(raw_weight)
        data[name].children = raw_children.split(", ") if raw_children else []

for node in data.values():
    node.children = [data[name] for name in node.children]
    for child in node.children:
        child.parent = node

root = next(node for node in data.values() if node.parent is None)
print(root.name)

current = root
while True:
    child_weights = [cumulative_weight(child) for child in current.children]
    if all_equal(child_weights):
        break
    else:
        #determine which child is the bad one, and make that the current node.
        #This will crash if there are exactly two children, so let's hope the input doesn't have any cases like that.
        current = odd_one_out(current.children, key=cumulative_weight)

siblings = [child for child in current.parent.children if child != current]
correct_cumulative_weight = cumulative_weight(siblings[0])
current_cumulative_weight = cumulative_weight(current)
correct_weight = current.weight + correct_cumulative_weight - current_cumulative_weight
print(correct_weight)
