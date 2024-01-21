import numpy as np
import math

def calculate_sin_values(start, end, total):

    x_values = np.linspace(start, end, total)
    sin_values = [(x, math.sin(x)) for x in x_values]
    return sin_values

def print_table(values):

    print(" x\t\t sin(x)")
    print("-" * 20)
    for x, sin_x in values:
        print(f"{x:.2f}\t {sin_x:.2f}")

def main():
    start = 0
    end = 2
    total = 1000
    sin_values = calculate_sin_values(start, end, total)
    print_table(sin_values)

if __name__ == "__main__":
    main()
