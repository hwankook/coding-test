from collections import deque

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

G = {v: [] for v in range(n)}
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    G[n1].append(n2)
    G[n2].append(n1)

exits = {}
for i in range(e):
    ei = int(input())  # the index of a gateway node
    exits[ei] = ei

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn

    stack = deque([si])

    found = False

    visited = [False] * n
    visited[si] = True

    prevIndex = [-1] * n

    while stack and not found:
        current = stack.popleft()
        for neighbor in G[current]:
            if not visited[neighbor]:
                prevIndex[neighbor] = current
                if neighbor in exits.keys():
                    current = neighbor
                    while prevIndex[current] != si:
                        current = prevIndex[current]
                    print(str(si) + ' ' + str(current))
                    found = True
                    break
                visited[neighbor] = True
                stack.append(neighbor)
