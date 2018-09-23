#----------------------------------------------------------
# Author: Maya Bishop
# Date: March 21, 2017
# Description: This program breaks down the payment of
#   your mortgage and shows it in two charts. One contains
#   every pay period and the other charts show the payments
#   for each year,  
# Input: User inputs the amount borrowed, the years it
#   will take to pay off the mortgage, the number of
#   payments made per year and the annual interest rate
#----------------------------------------------------------
#function to calculate the amount you pay for each period
def payAmount (p,y,ppy,ai):
    i = ai/ppy
    n = y*ppy
    a = (i*p)/(1-(1+i)**-n)
    return a
#function to print out the heading of the tables
def titles (year):
    print(format('Mortgage Payment Schedule - Year: '+str(year),'^60'))
    print(' ')
    print(format('PAY','^12')+format('PAYMENT','^12')+format('INTREST','^12')+format('PRINCIPAL','^12')+format('BALANCE','^12'))
    print(format('PERIOD','^12')+format('AMOUNT','^12')+format('PAID','^12')+format('DEDUCT','^12')+format('YR END','^12'))
    print('============================================================')
#prints title
print('MORTGAGE CALCULATOR PROGRAM BY MAYA BISHOP')
print('===========================================')
print(' ')
#creates variable are need to calculate the amount you pay for each period
principalAmount = float(input('Enter the amount borrowed: '))
years = float(input('Enter the length of the mortgage in years: '))
payPerYear = float(input('Enter the number of payments made per year: '))
annualIntrest = float(input('Enter the annual intrest rate: '))
annualIntrest = annualIntrest/100   #turns intrest rate into a precent
paymentAmount = payAmount(principalAmount,years,payPerYear,annualIntrest)   #calls function payAmount to find payment per period
print(' ')
print('===================================================')
print(' ')
#print main Chart headings
titles('All')
#calculate amounts need for each row of the charts
numPay = years*payPerYear
balance = principalAmount
periodIntrest = annualIntrest/payPerYear
totalCost = 0
#solves for each row and prints each row out
for p in range(1,int(numPay)+1):
    intrestPaid = balance*periodIntrest     #calculate intrest for each period
    totalCost = totalCost + intrestPaid     #figures out how much you paid in intrest
    principalDeduct = paymentAmount-intrestPaid     #figures out how much of the loan is paid off
    balance = balance - principalDeduct     #figure out the amount left to pay off 
    print(format(p,'6')+format(paymentAmount,'14,.2f')+format(intrestPaid,'12,.2f')+format(principalDeduct,'12,.2f')+format(balance,'12,.2f'))
print(' ')
print('Total borrowing Cost: $'+format(totalCost,',.2f'))
print(' ')
#reset balance
balance = principalAmount
#prints each year seperated
for y in range(1,int(years)+1):
    #only prints after you press the enter key
    enterDown = input('Press the Enter Key to continue .....')
    print(' ')
    titles(y)
    #prints only the pay periods for that year
    for p in range(1,int(payPerYear)+1):
        p = int(p + payPerYear*(y-1))     #calculates the pay period depending on the year
        intrestPaid = balance*periodIntrest     #calculate intrest for each period
        principalDeduct = paymentAmount-intrestPaid     #figures out how much of the loan is paid off
        balance = balance - principalDeduct     #figure out the amount left to pay off 
        print(format(p,'6')+format(paymentAmount,'14,.2f')+format(intrestPaid,'12,.2f')+format(principalDeduct,'12,.2f')+format(balance,'12,.2f'))
    print(' ')
print('Total borrowing Cost: $'+format(totalCost,',.2f'))
