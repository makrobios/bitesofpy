def print_hanging_indents(poem):
    indent = True
    lines = [line.strip() for line in poem.split('\n')]
    for line in lines:
        if not line.strip():
            indent = False
            continue
        if indent:
            print(f'    {line.strip()}')
        else:
            print(line)
            indent = True

            