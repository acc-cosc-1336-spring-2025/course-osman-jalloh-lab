# In src/homework/c_decisions/main.py

import decisions

def main():
    # Debugging: Print before input
    print("Starting input prompts")

    options = input("Enter the number of options: ")
    print(f"Options input: {options}")  # Debugging line to check user input
    options = float(options)  # Now convert it to a float

    total = input("Enter the total number: ")
    print(f"Total input: {total}")  # Debugging line to check user input
    total = float(total)  # Now convert it to a float

    # Get the ratio from get_options_ratio
    ratio = decisions.get_options_ratio(options, total)
    
    # Get the faculty rating
    rating = decisions.get_faculty_rating(ratio)
    
    # Display the result
    print(f"Faculty Rating: {rating}")

if __name__ == "__main__":
    main()


