#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Get all names defined in hidden_4 module
    names = dir(hidden_4)

    # Filter and print names that do not start with __
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
