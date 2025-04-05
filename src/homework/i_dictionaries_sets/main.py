from dictionary import get_p_distance_matrix


def get_input_sequences():
    """
    Prompts the user for a list of sequences (lists of strings).
    Each sequence is a string of characters.
    """
    sequences = []
    num_sequences = int(input("How many sequences do you want to input? "))
    
    for i in range(num_sequences):
        seq = input(f"Enter sequence {i + 1}: ")
        sequences.append(list(seq))  # Convert the string to a list of characters
    
    return sequences

def main():
    while True:
        print("\nMenu:")
        print("1. Get p-distance matrix")
        print("2. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            # Get the sequences from the user
            sequences = get_input_sequences()

            # Call the get_p_distance_matrix function
            result = get_p_distance_matrix(sequences)

            # Display the result
            print("\nP-distance matrix:")
            for row in result:
                print(row)
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == '__main__':
    main()


