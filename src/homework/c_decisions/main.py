from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

# Prompt user for input
options = float(input("Enter the number of options: "))
total = float(input("Enter the total: "))

# Calculate the ratio using the get_options_ratio function
result = get_options_ratio(options, total)

# Get the faculty rating using the result (ratio)
rating = get_faculty_rating(result)

# Display the rating
print(f"The faculty rating is: {rating}")
