#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]  # Skip the program name
    result = sum(int(arg) for arg in argv)

    print(result)
