# Mel Avina-Beltran
# ECS 32B H1 P4 4/11/23
# TidBit Computer Formula: Program should display a table, with appropriate headers, of a payment 
#                          schedule for the lifetime of the loan.

def tidBit(n):
    
    price = float(n)
    month = 1
    downPay = price*.10
    annIntRate = .12
    currentBal = price - downPay
    monthlyPay = (price-downPay)*.05
    monthlyInt = currentBal*annIntRate/12
    monthlyPrin = monthlyPay - monthlyInt
    pay = monthlyPay + monthlyPrin
    remainBal = currentBal - pay
    
    print('{:<7s} {:<20s} {:<20s} {:<20s} {:<15s} {:<20s}'.format('Month','Starting Balance', 'Interest to Pay', 'Principal to Pay','Payment','Ending Balance'))
    
    while remainBal > 0:
            monthlyInt = currentBal*annIntRate/12
            monthlyPrin = monthlyPay - monthlyInt
            pay = monthlyPay + monthlyPrin
            remainBal = currentBal - pay
            print('{:<7d} {:<20.2f} {:<20.2f} {:<20.2f} {:<15f} {:<20.2f}'.format(month, currentBal, monthlyInt, monthlyPrin, pay, remainBal))
            currentBal = currentBal - pay
            month = month + 1
        
tidBit(5000)
