# In src/homework/c_decisions/decisions.py

def get_options_ratio(options, total):
    # Function to calculate ratio of options/total
    return options / total

def get_faculty_rating(ratio):
    # Function to determine faculty rating based on ratio
    if 0.9 <= ratio <= 1:
        return "Excellent"
    elif 0.8 < ratio < 0.9:
        return "Very Good"
    elif 0.7 < ratio <= 0.8:
        return "Good"
    elif 0.6 < ratio <= 0.7:
        return "Needs Improvement"
    else:
        return "Unacceptable"

