# main.py

from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

def main():
    while True:
        print("Homework 3 Menu")
        print("1 - Factorial")
        print("2 - Sum odd numbers")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            num = int(input("Enter a number (1-9) to calculate its factorial: "))
            while num <= 0 or num >= 10:
                num = int(input("Please enter a number between 1 and 9: "))
            print(f"Factorial of {num} is {get_factorial(num)}")

        elif choice == "2":
            num = int(input("Enter a number (1-99) to sum odd numbers: "))
            while num <= 0 or num >= 100:
                num = int(input("Please enter a number between 1 and 99: "))
            print(f"Sum of odd numbers up to {num} is {sum_odd_numbers(num)}")

        elif choice == "3":
            exit_choice = input("Do you want to exit? (y/n): ")
            if exit_choice.lower() == "y":
                print("Exiting program.")
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
