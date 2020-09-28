"""
Codes for payroll calculations.
"""


# A function to prompt user for a numerical value and check if it is less than a minimum value
def getFloatValue(prompt, minimum) :
    goodValue = False           # Variable to loop at least once

    while (not goodValue) :
        try:
            userInput = input(prompt)   
            value = float(userInput)
            
            if ( value <= minimum ):
                print('***Invalid entry. Must be greater than zero. You entered:', userInput )
            else :
                goodValue = True
        except (ValueError):
            print('***Non-numeric value entered. Must be a number greater than zero. You entered:', userInput)

    return value


# A function to prompt user for a y/n answer (not case sensitive) and check if answer is valid
def getStringValue(prompt,string1, string2) :
    goodValue = False

    while (not goodValue) :
        stringValue = input(prompt)

        if (stringValue.lower() != string1) and (stringValue.lower() != string2) :
            print('***Invalid entry. Must be "y" or "n" (not case senstive). You entered:', stringValue)
        else :
            goodValue = True    

    return stringValue.lower()


# Get inputs from the user
employeeName = input('Enter employee name: ')
hoursWorked  = getFloatValue('Enter hours worked (greater than 0): ', 0)
hourlyRate   = getFloatValue('Enter hourly pay rate (grater than 0): ', 0)
taxExempt    = getStringValue('Is employee tax exempt? (Not case sensitive) [y/n]: ', 'y', 'n')


# Calculate an employee's net pay
deductionAmount = 0                     # Employee deduction amount

grossPay = hoursWorked * hourlyRate     # Employee gross pay amount

if (taxExempt == 'n') :
    deductionPercentage = getFloatValue('Enter percent deduction greater than zero and in whole number (e.g. 15 for 15%, not 0.15): ', 0)
    deductionAmount =  grossPay * ( deductionPercentage / 100 )

netPay = grossPay - deductionAmount     # Employee net pay amount
 

# Display results
print('====================================')
print('{:<16}  {}'            .format('Employee name:', employeeName) )
print('{:<16} {:>2} {:>10.2f}'.format('Hours worked:' , ' ', hoursWorked) )
print('{:<16} {:>2} {:>10.2f}'.format('Hourly rate:'  , '$', hourlyRate) )
print('====================================')
print('{:<16} {:>2} {:>10.2f}'.format('Gross pay:' , '$' , grossPay) )
print('{:<16} {:>2} {:>10.2f}'.format('Deductions:', '-$', deductionAmount) )
print('{:<16} {:>2}'          .format(''           , '--------------') )
print('{:<16} {:>2} {:>10.2f}'.format('Net pay:'   , '$' , netPay) )
