#!/usr/bin/python3
def print_tebahpla():
    """Print the ASCII alphabet in reverse order with alternating cases."""
    print(''.join(chr(122 - i) if i % 2 == 0 else chr(90 - i + 32) for i in range(26)))
    print_tebahpla()
