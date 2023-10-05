with open('input.txt', 'r') as f:
    print(f)
    for line in f:
        if line == '\n' or line == '\n\n' or line.startswith("("):
            continue
        elif line[0].isdigit():
            line.strip('\n')
            print("\n" + line, end="")
        else:
            line.strip('\n')
            print("*" + line, end="")