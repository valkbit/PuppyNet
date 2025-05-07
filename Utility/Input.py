def GatherInput(inputReason):
    inputIn = input(inputReason) # String Input
    try:
        return int(inputIn)  # Convert to int
    except ValueError:
        return None
