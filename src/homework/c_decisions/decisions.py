# src/homework/c_decisions/decisions.py

def get_options_ratio(option, total):
    """Returns the ratio of options divided by total."""
    if total == 0:  # Avoid division by zero
        return 0
    return option / total

def get_faculty_rating(ratio):
    """Returns the faculty rating based on the ratio."""
    if 0.9 <= ratio < 1:
        return "Excellent"
    elif 0.8 < ratio < 0.9:
        return "Very Good"
    elif 0.7 < ratio <= 0.8:
        return "Good"
    elif 0.6 < ratio <= 0.7:
        return "Needs Improvement"
    else:
        return "Unacceptable"
