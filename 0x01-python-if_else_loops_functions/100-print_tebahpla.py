#!/usr/bin/python3
def print_tebahpla():
    """Print the ASCII alphabet in reverse order with alternating cases."""
    for i in range(25, -1, -1):  # Start from 25 (z) to 0 (a)
        char = chr(122 - i)  # 122 is the ASCII value for 'z'
        if i % 2 == 0:
            print(char, end="")
        else:
            print(char.upper(), end="")
