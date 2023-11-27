

# This program is to calculate employee payroll.
# Date written: September 18, 2023.
# Arthr: Benjamin Osemene

# Required Constants defined.
HOURLY_PAY_RATE=17.50
COMM_SALES_PER_PERIOD= .06
COMM_ASS_PER_ITEM = .45
INCOME_TAX_RATE= .17
CPP_RATE= .0495
EI_RATE= .016
UNION_DUES_PER_PERIOD=12.00
MED_BENEFIT_RATE= .05


# Required inputs
EmployName = input("Enter the employee name:    ")
HoursWk = int(input("Enther the hours worked:   "))
TotSales = int(input("Enter the total sales:  "))
TotNumItems = int(input("Enter the total number of items:   "))

# Required calculations
RegularPay= HoursWk * HOURLY_PAY_RATE
SalesComm = TotSales * COMM_SALES_PER_PERIOD
AssemComm= TotNumItems* COMM_ASS_PER_ITEM 
TotComm = SalesComm + AssemComm
GrossPay = RegularPay+ TotComm
IncomeTax = GrossPay * INCOME_TAX_RATE
CPPDed = GrossPay * CPP_RATE
EIDed = GrossPay * EI_RATE
UnionDues= 12.00
MedicalB = GrossPay * MED_BENEFIT_RATE
TotDeductions = IncomeTax+ CPPDed + EIDed + UnionDues + MedicalB
NetPay = GrossPay - TotDeductions


# user display results
print(" Employee name:", EmployName)
print("Hours worked:", HoursWk)
print("Hourly pay rate:", HOURLY_PAY_RATE)
print("Commission sales:",  COMM_SALES_PER_PERIOD)
print("Commission assembly:",COMM_ASS_PER_ITEM )
print("Regular pay:", RegularPay)
print(" Sales commission:", SalesComm)
print("Assembly commission:", AssemComm)
print(" Total commission:", TotComm)
print(" Gross pay:", GrossPay)
print("Tax:",IncomeTax)
print("CPP:", CPPDed)
print("EI:", EIDed)
print("Union dues:", UnionDues)
print("Medical benefits:", MedicalB)
print("Total deductions:", TotDeductions)
print("Net pay:", NetPay)
















