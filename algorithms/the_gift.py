# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
c = int(input())

budget = []
for i in range(n):
    b = int(input())
    budget.append(b)
budget.sort()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

remainder = c
solution = [0] * len(budget)
for i, b in enumerate(budget):
    max_price = remainder // (n - i)
    if b < max_price:
        remainder -= b
        solution[i] = b
    else:
        if i == len(budget) - 1:
            solution[i] = remainder
            remainder = 0
        else:
            remainder -= max_price
            solution[i] = max_price

if 0 < remainder:
    print("IMPOSSIBLE")
else:
    for s in solution:
        print(s)
