# Mel Avina-Beltran
# ECS 32B H1 P4 4/11/23
# TidBit Computer Formula: Program should display a table, with appropriate headers, of a payment 
#                          schedule for the lifetime of the loan.

def tidBit(n):
    
    price = float(n)
    month = 1
    downPay = 0.10
    annIntRate = 0.12
    monthlyPay = 0.05
    
    currentBal = price - (price * downPay)
    monthlyPay = currentBal * monthlyPay
    monthlyInt = annIntRate/12

    print('{:<7s} {:<20s} {:<20s} {:<20s} {:<15s} {:<20s}'.format('Month','Starting Balance', 'Interest to Pay', 'Principal to Pay','Payment','Ending Balance'))
    
    while currentBal > 0:
            if currentBal < monthlyPay:
                lessInt = 0
                monthlyPrin = currentBal
                monthlyPay = currentBal
            else:
                lessInt = currentBal * monthlyInt
                monthlyPrin = monthlyPay - lessInt
            remainBal = currentBal - monthlyPrin
            print('{:<7d} {:<20.2f} {:<20.2f} {:<20.2f} {:<15f} {:<20.2f}'.format(month, currentBal, lessInt, monthlyPrin, monthlyPay, remainBal))
            currentBal = remainBal
            month = month + 1
        
tidBit(5000)
