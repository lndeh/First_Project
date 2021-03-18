# BMI code
print ("Lets check your health status")
weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in m: "))

BMI=(weight / (height * height))
print ("Your BMI is :" , BMI)

if BMI > 30 :
    print ("You are obese")
elif BMI > 25 :
    PRINT ("You are overweight")
elif BMI < 18.5 :
    print ("You are underweight")
else:
    print ("You are healthy")
