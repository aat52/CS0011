#If the worker has three or more dependents, then an additional $35 is withheld to cover the extra cost of health insurance beyond what the employer pays.


#print purpose of program
print("Calculate taxes, dues, gross pay, and net pay based on hours and dependents given.")

repeat = "y"

while True:
  #prompt user for inputs
  salary = float(input("Enter salary per hour: "))
  ov_salary = float((salary*1.50))
  hours = float(input("Number of hours worked in a week: "))
  #if loop to check if overtime
  if hours > 40:
    ov_hours = abs(hours-40)
    hours = 40
  else:
    ov_hours = 0
  dep_number = float(input("Number of dependents: "))

  #print regular hours and overtime
  print("Regular hours:", format(hours, '.2f'), "(at $"+str(format(salary,'.2f')), "per hour)")
  print("Overtime hours:", format(ov_hours, '.2f'), "(at $"+str(format(ov_salary,'.2f')), "per hour)")
  print("Total hours:", format(hours, ".2f"))

  #calculate and print gross pay
  gross = float((salary*hours)+(ov_salary*ov_hours))
  print("Gross pay: $"+format(gross,'.2f'))

  #calculate and print social security
  ss_tax = (gross*6)/100
  print("Social Security tax: $"+format(ss_tax,'.2f'))

  #calculate and print federal taxes
  fed_tax = (gross*14)/100
  print("Federal tax: $"+format(fed_tax,'.2f'))

  #calculate and print state taxes
  st_tax = (gross*5)/100
  print("State tax: $"+format(st_tax,'.2f'))

  #print union dues
  print("Union dues: $"+format(10,'.2f'))

  #check dependents
  if dep_number >= 3:
    dep_fee = float(35)
    print("Family health insurance: $"+format(dep_fee, ".2f"))
  else:
    dep_fee = float(0)


  #calculate and print total deductions
  total = float(ss_tax)+float(fed_tax)+float(st_tax)+10+dep_fee
  print("Total deductions: $"+format(total,'.2f'))

  #calculate and print net pay
  if total > gross:
    net = float(gross)-float(total)
    print("Dues and insurance obligations outstripped pay by $"+str(format(net,'.2f')))
  else:
     net = float(gross)-float(total)
     print("Net pay: $"+format(net,'.2f'))

  #ask user if they would like to repeat
  
  repeat = input("Would you like to calculate another week's pay? (y/n) ")
  if repeat=="n":
    break
