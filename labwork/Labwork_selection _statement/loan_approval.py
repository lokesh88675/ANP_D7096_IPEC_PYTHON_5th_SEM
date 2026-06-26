"""
Loan Approval System

 Problem Statement
   A bank evaluates loan applications using:
 • Credit Score ≥ 750 
 
 • Annual Income ≥ ₹8,00,000 
 ---------------------------------------------------------------
 • Existing Loan Amount ≤ ₹2,00,000  Conditions: 
 • All conditions satisfied → Approved 
 • Only one condition fails → Manual Review
 • More than one condition fails → Rejected
 --------------------------------------------------------------------
 Sample Input 
 Enter Credit Score: 780 
 Enter Annual Income: 750000 
 Enter Existing Loan Amount: 100000 
 ---------------------------------------------------------------
Sample Output Loan Status:
 Manual Review Reason: Income criteria not satisfied. 
 
"""
# -------------------- Input --------------------

credit_score = int(input("Enter Credit Score: "))
income = float(input("Enter Annual Income: "))
loan = float(input("Enter Existing Loan Amount: "))

# -------------------- Validation --------------------

if credit_score < 0 or credit_score > 900:
    exit("Invalid Input! Credit Score must be between 0 and 900.")

if income < 0:
    exit("Invalid Input! Income cannot be negative.")

if loan < 0:
    exit("Invalid Input! Existing Loan Amount cannot be negative.")

# -------------------- Checking Conditions --------------------

fail_count = 0
reason = ""

# Credit Score Condition
if credit_score < 750:
    fail_count += 1
    reason = "Credit Score criteria not satisfied."

# Income Condition
if income < 800000:
    fail_count += 1
    reason = "Income criteria not satisfied."

# Existing Loan Condition
if loan > 200000:
    fail_count += 1
    reason = "Existing Loan Amount criteria not satisfied."

# -------------------- Loan Decision --------------------

if fail_count == 0:
    print("Loan Status: Approved")

elif fail_count == 1:
    print("Loan Status: Manual Review")
    print("Reason:", reason)

else:
    print("Loan Status: Rejected")