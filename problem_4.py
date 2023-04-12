# Mel Avina-Beltran
# ECS 32B H1 P4 4/11/23
# TidBit Computer Formula: Program should display a table, with appropriate headers, of a payment 
#                          schedule for the lifetime of the loan.

def tidBit(n):
    
    month = 1
    downPay = n*.10
    annIntRate = .12
    currentBal = n - downPay
    monthlyPay = currentBal*.05
    
    while currentBal > 0:
        currentBal = currentBal - monthlyPay
        monthlyInt = currentBal*annIntRate/12
        monthlyPrin = monthlyPay - monthlyInt
        monthlyPay = monthlyPay + monthlyPrin // wrong
        remainBal = currentBal - monthlyPay
        print(month, currentBal, monthlyPay, monthlyInt, monthlyPrin, remainBal)
        month = month + 1
        
        
tidBit(5000)
