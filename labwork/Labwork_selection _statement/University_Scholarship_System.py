# University Scholarship System

percentage = float(input("Percentage: "))
income = float(input("Family Income: "))
discipline = input("Disciplinary Action (Y/N): ").upper()

# First check disqualification conditions
if income >= 800000 or discipline == "Y":
    print("Scholarship Awarded: No Scholarship")

else:
    # Scholarship based on percentage
    if percentage >= 95:
        print("Scholarship Awarded: 100%")

    elif percentage >= 90:
        print("Scholarship Awarded: 75%")

    elif percentage >= 85:
        print("Scholarship Awarded: 50%")

    elif percentage >= 80:
        print("Scholarship Awarded: 25%")

    else:
        print("Scholarship Awarded: No Scholarship")