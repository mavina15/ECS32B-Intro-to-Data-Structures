def recursive_gcd(a, b):
    
    a = int(a)
    b = int(b)
    
    if (a > 0) & (b > 0) and a > b: 
        
        dividend = a
        divisor = b
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

        
recursive_gcd(27, 18)
