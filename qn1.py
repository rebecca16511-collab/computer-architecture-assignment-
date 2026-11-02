def to_binary(n):
    return format(n & 0xFF, '08b')

def to_decimal(b):
    return b - 256 if b >= 128 else b

def arithmetic(a, b, operator):
    A = to_binary(a)
    B = to_binary(b)

    print("\nOperand A:", A)
    print("Operand B:", B)

    if operator == '+':
        result = (a + b) & 0xFF
        actual = a + b
    else:
        result = (a - b) & 0xFF
        actual = a - b

    print("Result in binary:", to_binary(result))
    print("Result in decimal:", to_decimal(result))

    if actual < -128 or actual > 127:
        print("Arithmetic Overflow: Yes")
    else:
        print("Arithmetic Overflow: No")


print("a) +48 + (+23)")
arithmetic(48, 23, '+')

print("\nb) (-46) - (-29)")
arithmetic(-46, -29, '-')