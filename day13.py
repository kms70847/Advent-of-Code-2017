import ast
import itertools

with open("13_input.txt") as file:
    d = ast.literal_eval("{" + file.read().replace("\n",",") + "}")

def trip(d, offset):
    maxdepth = max(d.keys())
    severity = 0
    caught = False
    for i in range(maxdepth+1):
        if i in d and (i+offset) % (d[i]*2-2) == 0:
            severity += d[i]*i
            caught = True
    return {"severity": severity, "caught": caught}

print(trip(d,0)["severity"])

for i in itertools.count():
    if not trip(d,i)["caught"]:
        print(i)
        break
