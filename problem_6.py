def recursive_gcd(a, b):
    
    a = max(a,b)
    b = min(a,b)
    
    dividend = a
    divisor = b
    
    if (a > 0) & (b > 0) : 
        
        q = int(dividend/divisor)
        r = dividend%divisor
            
        print(dividend, divisor, q, r)
            
        while r != 0:
            dividend = divisor
            divisor = r
            q = int(dividend/divisor)
            r = dividend%divisor
            print(dividend, divisor, q, r)
        print("GCD = ", divisor)

    else: 
        print("Try again")
        
recursive_gcd(32, 12)
