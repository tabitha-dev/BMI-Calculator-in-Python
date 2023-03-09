# BMI calculator in Python
def calculate_bmi(weight_lbs, height_ft, height_in):
    # Convert height to inches
    height_total_in = height_ft * 12 + height_in
    
    # Calculate BMI
    bmi = (weight_lbs / (height_total_in ** 2)) * 703
    
    # Round BMI to two decimal places
    bmi_rounded = round(bmi, 2)
    
    return bmi_rounded

# Get user's weight in pounds
weight_lbs = float(input("Enter your weight in pounds: "))

# Get user's height in feet and inches
height_ft = int(input("Enter your height in feet: "))
height_in = int(input("Enter your height in inches: "))

# Calculate user's BMI
bmi = calculate_bmi(weight_lbs, height_ft, height_in)

# Print BMI result
print("Your BMI is:", bmi)
