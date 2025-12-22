import copy

# Initial boundaries
S = ['Null', 'Null', 'Null', 'Null', 'Null', 'Null']
G = [['?', '?', '?', '?', '?', '?']]

def is_consistent(h, x):
    for i in range(len(h)):
        if h[i] != '?' and h[i] != x[i]:
            return False
    return True

def positive_example(S, G, x):
    # Update S
    for i in range(len(S)):
        if S[i] == 'Null':
            S[i] = x[i]
        elif S[i] != x[i]:
            S[i] = '?'

    # Remove inconsistent hypotheses from G
    G[:] = [g for g in G if is_consistent(g, x)]

def negative_example(S, G, x):
    new_G = []

    for g in G:
        if is_consistent(g, x):
            for i in range(len(g)):
                if g[i] == '?':
                    if S[i] != '?' and S[i] != x[i]:
                        new_h = g.copy()
                        new_h[i] = S[i]
                        new_G.append(new_h)
        else:
            new_G.append(g)

    G[:] = new_G

# Training instances
instance1 = ['sunny', 'warm', 'normal', 'strong', 'warm', 'same']   # +
instance2 = ['sunny', 'warm', 'high', 'strong', 'warm', 'same']     # +
instance3 = ['rainy', 'cold', 'high', 'strong', 'warm', 'change']   # -
instance4 = ['sunny', 'warm', 'high', 'strong', 'cool', 'change']   # +

# Apply algorithm
positive_example(S, G, instance1)
print("After Instance 1")
print("S =", S)
print("G =", G)

positive_example(S, G, instance2)
print("\nAfter Instance 2")
print("S =", S)
print("G =", G)

negative_example(S, G, instance3)
print("\nAfter Instance 3")
print("S =", S)
print("G =", G)

positive_example(S, G, instance4)
print("\nAfter Instance 4")
print("S =", S)
print("G =", G)
=========================================================================
OUTPUT:
After Instance 1
S = ['sunny', 'warm', 'normal', 'strong', 'warm', 'same']
G = [['?', '?', '?', '?', '?', '?']]

After Instance 2
S = ['sunny', 'warm', '?', 'strong', 'warm', 'same']
G = [['?', '?', '?', '?', '?', '?']]

After Instance 3
S = ['sunny', 'warm', '?', 'strong', 'warm', 'same']
G = [['sunny', '?', '?', '?', '?', '?'], ['?', 'warm', '?', '?', '?', '?'], ['?', '?', '?', '?', '?', 'same']]

After Instance 4
S = ['sunny', 'warm', '?', 'strong', '?', '?']
G = [['sunny', '?', '?', '?', '?', '?'], ['?', 'warm', '?', '?', '?', '?']]
============================================================
