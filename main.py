print("This program calculates your Body Mass Index")
num1 = float(input("Enter your weight (kg): "))
num2 = float(input("Enter your height (m): "))
bmi = round((num1 / (num2**2)),2)
if bmi < 18.5: 
    print("Your BMI is " + str(bmi) + " (underweight)")
elif  18.5 <= bmi < 23:
    print("Your BMI is " + str(bmi) + " (normal)")
elif 23 <= bmi < 25:
    print("Your BMI is " + str(bmi) + " (overweight)")
else:
   print("Your BMI is " + str(bmi) + " (obese)")
 