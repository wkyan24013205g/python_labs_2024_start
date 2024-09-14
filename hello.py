# print("Hellow World")

def print_integers(n):
    if n < 0:
        raise ValueError("Input must be a positive integer")
    for i in range(n + 1):
        print(i)

print_integers(10)