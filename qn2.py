def ROR(num, count):
    print("\nRotate Right Without Carry (ROR)")
    print("Original:", format(num, '08b'))

    for i in range(count):
        lsb = num & 1
        num = (num >> 1) | (lsb << 7)
        print("Step", i + 1, ":", format(num, '08b'))

    print("Final Result:", format(num, '08b'))


def RCR(num, count, carry):
    print("\nRotate Right With Carry (RCR)")
    print("Original:", format(num, '08b'))
    print("Initial Carry:", carry)

    for i in range(count):
        new_carry = num & 1
        num = (num >> 1) | (carry << 7)
        carry = new_carry

        print("Step", i + 1, ":",
              format(num, '08b'),
              "Carry:", carry)

    print("Final Result:", format(num, '08b'))
    print("Final Carry:", carry)


num = int('11010101', 2)

ROR(num, 2)

RCR(num, 2, 0)