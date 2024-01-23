def magic_calculation(a, b):
    from calculator_1 import add, sub
    if a < b:
        return add(a, b)
    else:
        return sub(a, b)
