from enum import Enum

class BMI(Enum):
    UNDER_WEIGHT = 18.5
    NORMAL_WEIGHT = 25
    SLIGHTLY_OVERWEIGHT = 30
    OBESE = 35

weight = int(input("Enter weight: "))
height = float(input("Enter height: "))
bmi = round(weight / (height * height))

if bmi < BMI.UNDER_WEIGHT.value:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < BMI.NORMAL_WEIGHT.value:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < BMI.SLIGHTLY_OVERWEIGHT.value:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < BMI.OBESE.value:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
