def is_arthmetic(a, b, c):
    diff = b - a
    return c == a + 2 * diff

def is_geometric(a, b, c):
    return (b/a) == (c/b)

while True:
    input_str = input()
    a, b, c = [int(x) for x in input_str.split()]
    if a == b == c == 0:
        break
    else:
        if is_arthmetic(a, b, c):
            print("AP", c + (b - a))
        elif is_geometric(a, b, c):
            print("GP", int(c * (b/a)))
