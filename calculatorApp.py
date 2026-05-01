def basicCalc(inp):
    inp[0] = int(inp[0])
    inp[2] = int(inp[2])
    if inp[1] == "+":
        return inp[0] + inp[2]
    if inp[1] == "-":
        return inp[0] - inp[2]
    if inp[1] == "*":
        return inp[0] * inp[2]
    if inp[1] == "/":
        return inp[0] / inp[2]