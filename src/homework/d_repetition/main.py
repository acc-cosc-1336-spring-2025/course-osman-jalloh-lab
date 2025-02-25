import repetition

def display_menu():
        print("Homework 3 Menu")
        print("1 - Factorial")
        print("2 - Sum odd numbers")
        print("3 - Exit")
def ask_to_continue():
        while True:
             choice = input('do you want to continue? (yes/no):').strip().lower()
             if choice == "yes":
                  return True
             elif choice == "no":
                  return False
             else:
                  print("invalid input")
def run_menu():
    choice = "0"
    while choice != "3":
        display_menu()
        
        choice = input("Enter your choice(1,2,3): ")
        if choice == "1":
            num = int(input("Enter a number (1-9) to calculate its factorial: "))
            while num < 1 or num > 9:
                num = int(input("Please enter a number between 1 and 9: "))
            print(f"Factorial of {num} is {repetition.get_factorial(num)}")
        
        elif choice == "2":
            num = int(input("Enter a number (1-99) to sum odd numbers: "))
            while num < 1 or num > 99:
                num = int(input("Please enter a number between 1 and 99: "))
            print(f"Sum of odd numbers up to {num} is {repetition.sum_odd_numbers(num)}")
        
        elif choice == "3":
            print ("exiting the program")
                
        else:
            print("Invalid choice. Please try again.")
        
      
        
        if choice != "3"and not ask_to_continue():
            print("exiting program.")
            break

if __name__ == "__main__":
    run_menu()
