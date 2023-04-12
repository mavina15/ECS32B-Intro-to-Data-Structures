# Mel Avina-Beltran
# ECS 32B H1 P4 4/11/23
# TidBit Computer Formula: Program should display a table, with appropriate headers, of a payment 
#                          schedule for the lifetime of the loan.

def tidBit(n):
    
    downPay = .10*n
    annIntRate = .12
    monthPay = (n-downPay)*.05
    month = 1
    currentBal = n
    
    while True:
        currentBal = n - downPay
        monthlyInt = currentBal * annIntRate / 12
        monthlyPrin = monthPay - monthlyInt 
        remainBal = currentBal - monthPay
        
        print(month, n, currentBal, monthlyInt, monthlyPrin, monthPay, remainBal)
        return month, n, currentBal, monthlyInt, monthlyPrin, monthPay, remainBal
        
        if remainBal > 0:
            month += 1
            currentBal = n - downPay
            monthlyInt = currentBal * annIntRate / 12
            monthlyPrin = monthPay - monthlyInt 
            remainBal = currentBal - monthPay
            
            print(month, n, currentBal, monthlyInt, monthlyPrin, monthPay, remainBal)
            return month, n, currentBal, monthlyInt, monthlyPrin, monthPay, remainBal
        else:
            break
    print("done")
    
tidBit(5000)
