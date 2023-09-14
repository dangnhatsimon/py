

def my_min(x, *args):
    if len(args) == 1:
        if x < args[0]:
            return x
        else:
            return args[0]
    y, *args = args
    print(y)
    print(*args)
    if x < y:
        print(x)
        return my_min(x, *args)
    else:
        print(y)
        return my_min(y, *args)

print(my_min(8, 13, 4, 42, 120, 7))