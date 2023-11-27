

# This program is to prepoare St. John's Marina and Yacht club members receipt.
# Date written: September 27, 2023 - October6, 2023.
# Author: Benjamin Osemene

# Constants
EVEN_NUM_SITES_COST = 80.00              # 80$ as at the time of writing this program
ODD_NUM_COST = 120.00                    # 120$ as at the time of writing this program
ALT_MEM_COST = 5.00                      # 5$ as at the time of writing this program
WKLY_SITE_CLEANING_CHRG = 50.00               # 50$ as at the time of writing this program
VIDEO_SURVEILLANCE_CHRG = 35.00          # 35$ as at the time of writing this program
HST_RATE = .15                           # 15% as at the time of writing this program
STD_MEM_DUES = 75.00                     # 75$ as at the time of writing this program
EXEC_MEM_DUES = 150.00                   # 150$ as at the time of writing this program
PROCESSING_FEE = 59.99                   # 59.99$ as at the time of writing this program
CAN_FEE_RATE = .6                        # 60% as at the time of writing this program

# User Input
SiteNum = input("Enter site number (1-100):  ")
MemName = input("Enter member name:  ")
StAdd = input("Enter street address:  ")
City = input("Enter the city:  ")
Prov = input("Enter province(XX):  ").upper()
PostCode = input("Enter post code(X#X#X#):  ").upper()
PhoneNum = input("Enter the phone number(###-###-####):  ")
CellNum = input("Enter cell number(###-###-####):  ")
MemType = input("Enter membership type( S,E):  ").upper()
NumAltMem = input("Enter number of alternate members(family/frinds):  ")
WklySiteCleaning = input("Would you like weekly site cleaning(Y/N):  ").upper()
VideoSurv = input("Would you like video surveillance(Y/N):  ")

# Program Calculation
if SiteNum == 1:
    OddNumChrg = ODD_NUM_COST
else:
    EvenNumChrg = EVEN_NUM_SITES_COST

SiteChrg = EVEN_NUM_SITES_COST + ODD_NUM_COST  

if WklySiteCleaning == "Y":
    WklyCleaningCost = WKLY_SITE_CLEANING_CHRG
else: 
    WklyCleaningCost = 0

if VideoSurv == "Y":
    VideoSurvCost = VIDEO_SURVEILLANCE_CHRG
else:
    VideoSurvCost = 0

ExtraCharges =  WKLY_SITE_CLEANING_CHRG + VIDEO_SURVEILLANCE_CHRG

SubTotal= SiteChrg + ExtraCharges

HSTCal = SubTotal * HST_RATE

TotMonthlyChrg = SubTotal + HSTCal

MonthlyDues = STD_MEM_DUES + EXEC_MEM_DUES
TotMonthlyFees = TotMonthlyChrg + MonthlyDues

TotYearlyFees = TotMonthlyFees * 12

MonthlyPayment = (TotYearlyFees + PROCESSING_FEE)/ 12

CanFee = (SiteChrg * CAN_FEE_RATE )* 12



print()

# Invoice for the member

print(f"    St. John's Marina & Yacht Club")
print(f"       Yearly Member Receipt")
print()
print(f" ----------------------------------------------")
print()
print(f" Client Name: {MemName:<15s}")
print(f" Addres:      {StAdd:<11s}")
print()
print(f" Phone: {PhoneNum:<10s} (H)")
print(f"        {CellNum:<10s}  (C)")
print()
print(f" Site:  {SiteNum:>1} Member type: {MemType:<1s}")  
print()
print(f" Alternate members:             {NumAltMem:>1s}")
print(f" Weekly site cleaning:   {WklySiteCleaning:<1s}")
print(f" Video surveillance:            {VideoSurv:<1s}")
print()
SiteChrgDsp = "${:,.2f}".format(SiteChrg)
print(f" Site Charges:                {SiteChrgDsp:>9s}")
ExtraChargesDsp = "${:,.2f}".format(ExtraCharges)
print(f" Extra Charges:           {ExtraChargesDsp:>7s}")
print(f"                           --------------------")
SubTotalDsp = "${:,.2f}".format(SubTotal)
print(f" Subtotal:                    {SubTotalDsp:>9s}")
HSTCalDsp = "${:,.2f}".format(HSTCal)
print(f" Sales tax (HST):              {HSTCalDsp::>7s}")
print(f"                             ------------------")
TotMonthlyChrgDsp = "${:,.2f}".format(TotMonthlyChrg)
print(f" Total monthly charges:  {TotMonthlyChrgDsp:>9s}")
MonthlyDuesDsp = "${:,.2f}".format(MonthlyDues)
print(f" Monthly dues:              {MonthlyDuesDsp:>7s}")
print(f"                              ------------------")
TotMonthlyFeesDsp = "${:,.2f}".format(TotMonthlyFees)
print(f" Total monthly fees:     {TotMonthlyFeesDsp:>9s}")
TotYearlyFeesDsp = "${:,.2f}".format(TotYearlyFees)
print(f" Total yearly fees:      {TotYearlyFeesDsp:>10s}")
print()
MonthlyPaymentDsp = "${:,.2f}".format(MonthlyPayment)
print(f" Monthly payment:        {MonthlyPaymentDsp:>9s}")
print()
print(f" -----------------------------------------------")
print()
print(f" Issued: YYYY-MM-DD")
print(f" HST Reg No: 549-33-5849-4720-9885")
print()
CanFeeDsp = "${:,.2f}".format(CanFee)
print(f" Cancellation fee:              {CanFeeDsp:>9s}")
print()