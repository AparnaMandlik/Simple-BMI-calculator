#Simple BMI calculator using python

def bodymassindex(height, weight):
    return round((weight / height**2),2)


height = float(input("Enter your height in meters: "))
weight= float(input("Enter your weight in kg: "))


print("Welcome to the BMI calculator.")

BMI = weight/height*height
print("Your BMI is: ", BMI)


if BMI <= 18.5:
    print("You are underweight.")
elif 18.5 < BMI<= 24.9:
    print("Your weight is normal.")
elif 25 <BMI <= 29.29:
    print("You are overweight.")
elif 30<BMI<34.9:
    print("you are Obesity(class1)")
elif 35<BMI<39.9:
    print("you are Obesity(class2)")
else:
    print("You are  severely obese.")
