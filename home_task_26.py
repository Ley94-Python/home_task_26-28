
def rec(a, b):
    if b == 0:
        return 1
    else:
        return a * rec(a, b -1)
a, b = 3, 5
print(rec(a, b))
