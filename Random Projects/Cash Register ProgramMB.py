#----------------------------------------------------------
# Author: Maya Bishop
# Date: Feb 10, 2017
# Description: The Program calculates the HST tax,
#   total amount of purchase, the total change and
#   denomination of change to be given
# Input: User input of the cost of an item and the cash
#   tendered.
#----------------------------------------------------------
print ("CASH REGISTER PROGRAM BY Maya Bishop")
print(' ')
#using the cost of an item and the HST for that item to figure out the cost
#print both item and total costs and HST with proper formating(2 decimal places and rounding ect.)
itemCost = round(float(input('Enter purchase amount: ')), 2)
print(' ')
hst = round(itemCost*0.13, 2)
totalCost = round(itemCost+hst, 2)
print (format("Item Cost:",'<11')+format("$",'>3'),format(itemCost,">7.2f"))
print (format("HST:",'<11')+format("$",'>3'),format(hst,">7.2f"))
print('--------------------------------')
print (format("Total Cost:",'<11')+format("$",'>3'),format(totalCost,">7.2f"))
print(' ')
#use the total cost and cash given to find the change given to the customer
#print out total change(2 decimal places and rounding ect.)
cashTendered = round(float(input('Enter cash tendered: ')), 2)
totalChange = round(cashTendered - totalCost, 2)
print(' ')
print("Total Change:",format(totalChange,">7.2f"))
print('--------------------------------')
#Use interger division and modules to breakdown the change given to the customer and print out the change breakdown
fiftyDollar = totalChange//50
totalChange = totalChange%50
print(format("$50:",">4"),format(fiftyDollar,'3.0f'))

twentyDollar = totalChange//20
totalChange = totalChange%20
print(format("$20:",">4"),format(twentyDollar,'3.0f'))

tenDollar = totalChange//10
totalChange = totalChange%10
print(format("$10:",">4"),format(tenDollar,'3.0f'))

fiveDollar = totalChange//5
totalChange = totalChange%5
print(format("$5:",">4"),format(fiveDollar,'3.0f'))

twoDollar = totalChange//2
totalChange = totalChange%2
print(format("$2:",">4"),format(twoDollar,'3.0f'))

oneDollar = totalChange//1
totalChange = totalChange%1
print(format("$1:",">4"),format(oneDollar,'3.0f'))

twentyfiveCent = totalChange//0.25
totalChange = totalChange%0.25
print(format("25"+chr(162)+":",">4"),format(twentyfiveCent,'3.0f'))

tenCent = totalChange//0.10
totalChange = totalChange%0.10
print(format("10"+chr(162)+":",">4"),format(tenCent,'3.0f'))

fiveCent = totalChange//0.05
totalChange = totalChange%0.05
print(format("5"+chr(162)+":",">4"),format(fiveCent,'3.0f'))

oneCent = totalChange//0.01
totalChange = totalChange%0.01
print(format("1"+chr(162)+":",">4"),format(oneCent,'3.0f'))
