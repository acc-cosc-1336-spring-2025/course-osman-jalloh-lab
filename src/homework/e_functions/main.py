def convert_seconds_to_time(seconds):
    # Calculate hours
    hours = seconds // 3600
    
    # Calculate minutes
    minutes = (seconds % 3600) // 60
    
    # Calculate remaining seconds
    remaining_seconds = seconds % 60
    
    # Format the time as HH:MM:SS with leading zeros
    time_format = f"{hours:02}:{minutes:02}:{remaining_seconds:02}"
    
    return time_format

# Example input: 3800 seconds
input_seconds = 3800
time = convert_seconds_to_time(input_seconds)
print(time)  # Expected Output: 01:03:20
