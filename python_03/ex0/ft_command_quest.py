import sys


def main():
    arguments = sys.argv[1:]
    print("=== Command Quest ===")
    if not arguments:
        print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    if len(arguments) >= 1:
        x = 1
        print(f"Arguments received: {len(arguments)}")
        for num in arguments:
            print(f"Arguments {x}: {num}")
            x += 1
    print(f"Total arguments: {len(sys.argv)}")


main()
