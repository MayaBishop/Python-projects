#---------------------------------------------------------------
# Author: Maya Bishop
# Date: March 7, 2017
# Description: The program computes and employee's weekly pay 
#   and produces a pay slip showing gross pay, deductions, 
#   and net pay.
# Input: User inputs the employee's name, their hourly rate of
#   pay, the number of hours worked that week, the employee's
#   tax category, a $10 donation to United Way, and whether to
#   add another employee's information.
#---------------------------------------------------------------
print("Maya's Employee Payslip Calculator")
employeesProcessed = 0
while(True):            #repeats for every employee
    print("-----------------------------------")
    print(" ")
    #ask for imputs
    name = input("Employee Name: ")
    hourlyRate = float(input("Hourly Rate of Pay: "))
    hoursWorked = float(input("Hours worked: "))
    print("Tax Category: (A: No Tax, B: 10%, C: 20%, D: 29%, E: 35%)")
    taxCategory = input("Enter A,B,C,D, or E: ")
    unitedWayDonation = input("United Way Donation? Y or N: ")
    #calculate for gross pay (double pay for extra hours) 
    if hoursWorked > 40:
        extraHours = hoursWorked - 40
        hoursWorked = 40
        grossPay = hourlyRate*hoursWorked + hourlyRate*extraHours*2
    else:
        grossPay = hourlyRate*hoursWorked
    #calculate for tax based of input
    if taxCategory == "a" or taxCategory == "A":
        tax = grossPay*0
    elif taxCategory == "b" or taxCategory == "B":
        tax = grossPay*0.10
    elif taxCategory == "c" or taxCategory == "C":
        tax = grossPay*0.20
    elif taxCategory == "d" or taxCategory == "D":
        tax = grossPay*0.29
    else:
        tax = grossPay*0.35
    #united way donation
    if unitedWayDonation == 'y' or unitedWayDonation == "Y":
        donation = 10
    else:
        donation = 0
    #find net pay
    netPay = grossPay - tax - donation
    #print out pay slip
    print("-----------------------------------")
    print(" ")
    print("Employee PaySlip for", name)
    print("-----------------------------------")
    print(format("Gross Pay:", '<10'), format(round (grossPay, 2), '10.2f'))
    print(format("Taxes:", '<10'), format(round (tax, 2), '10.2f'))
    print(format("Donation:", '<10'), format(donation, '10.2f'))
    print(format("===========", '>22'))
    print(format("Net Pay:", '<10'),format(round (netPay, 2), '10.2f'))
    print(" ")
    #increase employees processed for each loop and stop looping if there is no other employees
    employeesProcessed += 1
    yorn = input('Enter another employee? (y or n):')
    if yorn == "y" or yorn == "Y":
        continue
    else:
        break
#print out final message that includes the amount of employees processed
print(" ")
print('Thank you! Employees processed in this session:',employeesProcessed)
