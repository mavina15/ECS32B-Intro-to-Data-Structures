# Mel Avina-Beltran
# ECS 32B H1 P4 4/11/23
# TidBit Computer Formula: Program should display a table, with appropriate headers, of a payment 
#                          schedule for the lifetime of the loan.

def tidBit(n):
    
    # change string to float var
    price = float(n)
    
    # initlize vars
    month = 1
    downPay = 0.10
    annIntRate = 0.12
    monthlyPay = 0.05
    
    # formulas needed before recusive statement
    currentBal = price - (price * downPay)
    monthlyPay = currentBal * monthlyPay
    monthlyInt = annIntRate/12
    
    # print table headers
    print('{:<7s} {:<20s} {:<20s} {:<20s} {:<15s} {:<20s}'.format('Month','Starting Balance', 'Interest to Pay', 'Principal to Pay','Payment','Ending Balance'))
    
    # while loop checks if currentBal is greater than 0
    while currentBal > 0:
            
            # nested if else statement
            if currentBal < monthlyPay:
                
                # if balance is less than monthly payment no interest is charges and balance is payed off
                lessInt = 0
                monthlyPrin = currentBal
                monthlyPay = currentBal
            else:
                
                # else interest is added to monthly payment 
                lessInt = currentBal * monthlyInt
                monthlyPrin = monthlyPay - lessInt
            remainBal = currentBal - monthlyPrin
            
            # prints rows of info from loop to table
            print('{:<7d} {:<20.2f} {:<20.2f} {:<20.2f} {:<15f} {:<20.2f}'.format(month, currentBal, lessInt, monthlyPrin, monthlyPay, remainBal))
            currentBal = remainBal
            month = month + 1
        
tidBit(5000)
