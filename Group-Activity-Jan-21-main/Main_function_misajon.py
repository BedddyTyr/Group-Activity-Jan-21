from Addition_Samuya import add
from Multiplication_MARABE import multiply as mul
from Sonquipal_Division import divide as div
from Orencia_Subtraction import subtract as sub


def main():
    print("Persistent Calculator")
    print("Type 'q' at any time to quit.\n")

    while True:
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter choice (1-4 or q): ").strip().lower()
        if choice == "q":
            print("Goodbye!")
            break

        try:
            a = input("Enter first number: ").strip()
            if a.lower() == "q":
                break
            b = input("Enter second number: ").strip()
            if b.lower() == "q":
                break

            a = float(a)
            b = float(b)

            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = sub(a, b)
            elif choice == "3":
                result = mul(a, b)
            elif choice == "4":
                result = div(a, b)
            else:
                print("Invalid choice.\n")
                continue

            print(f"Result: {result}\n")

        except ValueError as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
