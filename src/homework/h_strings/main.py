from strings import get_hamming_distance, get_dna_complement

def main():
    while True:
        print("\n1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            dna1 = input("Enter first DNA string: ").upper()
            dna2 = input("Enter second DNA string: ").upper()
            try:
                print("Hamming Distance:", get_hamming_distance(dna1, dna2))
            except ValueError as e:
                print(e)

        elif choice == "2":
            dna = input("Enter DNA string: ").upper()
            print("DNA Complement:", get_dna_complement(dna))

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
