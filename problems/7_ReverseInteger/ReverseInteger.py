
# my string reversal solution - not the most efficient, but readable and concise 

def solution_1(x):
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    # Handle sign
    sign = -1 if x < 0 else 1
    x_str = str(abs(x))
    
    # Reverse the string and convert back
    reversed_str = x_str[::-1]
    result = sign * int(reversed_str)  
    
    # Check bounds
    return result if INT_MIN <= result <= INT_MAX else 0



# ----------- Test ----------

x = -123
print(f"x: {x} is now {solution_1(x)}")
