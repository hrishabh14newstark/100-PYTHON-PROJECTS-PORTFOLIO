"""
15: BMI Calculator
Simple math and conditional logic based on weight and height.
"""
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

if __name__ == "__main__":
    bmi, cat = calculate_bmi(70, 1.75)
    print(f"BMI: {bmi:.2f} ({cat})")
