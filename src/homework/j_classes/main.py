from class_a import Die
def main():
    die = Die()
    while True:
        user_input = input("Roll the die? (yes/no): ").strip().lower()
        if user_input in ['no', 'n', 'exit', 'quit']:
            print("Exiting the program.")
            break
        elif user_input in ['yes', 'y']:
            die.roll()
            print(die)
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    main()

