from lists import get_lowest_list_value,get_highest_list_value

def main():
    numbers = []
    while True:
        print("Menu:")
        print("1- Show the list low/high values")
        print("2- Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                value = int(input("Enter a list value: "))
                numbers.append(value)
                another = input("Do you want to enter another value? (yes/no): ")
                if another.lower() != 'yes':
                    break
            
            lowest = get_lowest_list_value(numbers)
            highest = get_highest_list_value(numbers)
            print(f"The lowest value is: {lowest}")
            print(f"The highest value is: {highest}")
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == '__main__':
    main()
