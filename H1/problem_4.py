# Mel Avina-Beltran
# ECS 32B H1 P4 1/20/23
# TidBit Computer Formula: Program should display a table, with appropriate headers, of a payment 
#                          schedule for the lifetime of the loan.

def storeCalc(price):
    
    price = float(price)
    month = 1
    interest = 0.12
    downPay = 0.10
    monthPay = 0.05

    currentBal = price - (price * downPay)

    monthPay = monthPay * currentBal
    monthInt = interest / 12

    # main header
    print('{:<15s} {:<20s} {:<20s} {:<20s} {:<20s} {:<20s}'.format('Month','Starting Balance', 'Interest to Pay', 'Principal to Pay','Payment','Ending Balance'))
    while currentBal > 0:                                   # recursive function that ends the balance is 0
        if currentBal < monthPay:                           # if the balance is less than the monthlypayment no interest is charged
            intAmount = 0
            principal = currentBal
            monthPay = currentBal
        else:                                               # else interest is charged
            intAmount = currentBal * monthInt
            principal = monthPay - intAmount
        endingBal = currentBal - principal                  # printed lines with each month's information
        print('{:<15d} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f}'.format(month, currentBal, intAmount, principal, monthPay, endingBal))
        currentBal = endingBal                              # function continues to next month if balance is remaining
        month = month + 1



storeCalc(5000)
