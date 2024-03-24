def format_time(hours, minutes, seconds):
    if len(str(hours)) == 1:
        hours = f"0{hours}"
    if len(str(minutes)) == 1:
        minutes = f"0{minutes}"
    if len(str(seconds)) == 1:
        seconds = f"0{seconds}"
    return f"{hours}:{minutes}:{seconds}"