import sys

def add_numbers(a, b):
    return a + b

def main():
    if len(sys.argv) < 3:
        print("Please provide two numbers.")
        return

    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

    result = add_numbers(num1, num2)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
