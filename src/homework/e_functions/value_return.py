def get_hours(epoch_seconds):
    # Calculate hours (3600 seconds per hour)
    hours = (epoch_seconds // 3600) % 24
    return hours

def get_minutes(epoch_seconds):
    # Calculate minutes (60 seconds per minute)
    minutes = (epoch_seconds % 3600) // 60
    return minutes

def get_seconds(epoch_seconds):
    # Calculate remaining seconds
    seconds = epoch_seconds % 60
    return seconds
