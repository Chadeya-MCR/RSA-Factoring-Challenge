import sys

def factorize(number):
    factors = []
    for i in range(2, number//2 + 1):
        if number % i == 0:
            factors.append((i, number // i))
    return factors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        numbers = file.readlines()

    for num in numbers:
        number = int(num)
        factor_pairs = factorize(number)
        for pair in factor_pairs:
            print(f"{number}={pair[0]}*{pair[1]}")
