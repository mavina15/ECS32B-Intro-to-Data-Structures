def recursive_gcd(a, b):
    
    # gets the bigger and smaller number to avoid another loop/recursion statement
    a = max(a,b)
    b = min(a,b)
    
    # intilizes dividend and divisor
    dividend = a
    divisor = b
    
    # if else statment checks for only positive values
    if (a > 0) & (b > 0) : 
        
        # initialized quotient and remainder, q must be an integer since we need it to be a whole number, q uses modulo operator
        q = int(dividend/divisor)
        r = dividend%divisor
            
        print(dividend, divisor, q, r)
        
        # while loop to continue finding the gcd until the remainder is 0
        while r != 0:
            dividend = divisor
            divisor = r
            q = int(dividend/divisor)
            r = dividend%divisor
            print(dividend, divisor, q, r)
        print("GCD = ", divisor)

    else: 
        print("Try again")
        
recursive_gcd(a, b)
