def large_power(base, exponent):
    # Calculate the power of base raised to exponent
    result = base ** exponent
    
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

# Example usage:
print(large_power(5, 3))  
print(large_power(10, 4))  
