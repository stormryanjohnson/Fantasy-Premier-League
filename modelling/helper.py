def round_to_nearest_5(number):
    
    # Calculate the remainder when dividing the number by 5
    remainder = number % 5
    
    # If remainder is less than 2.5, round down; otherwise, round up
    if remainder < 2.5:
        return number - remainder
    else:
        return number + (5 - remainder)