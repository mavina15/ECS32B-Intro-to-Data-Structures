# Mel Avina-Beltran
# ECS 32B H1 P5 1/20/23
# Pay Roll: Program that inputs a filename from the user and prints a report to the terminal of 
#           the wages paid to the employees for the given period.

def employ(lastName, hourlyWage, hoursWork):                                        # inputs 

    print('{:<12s} {:>10s} {:>10s}'.format('Name', 'Hours', 'Total Pay'))           # main header
    hoursWork = int(hoursWork)
    totalPay = hoursWork * hourlyWage
    print('{:<12s} {:>10d} {:>10.2f}'.format(lastName, hoursWork, totalPay))        # employee report

    return lastName, hoursWork, totalPay

#employ('Avina', 56, 983)
