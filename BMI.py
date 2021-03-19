# BMI code
h = 0
w = 0

def getWeight():   
    print ("Lets check your health status")
    weight = float(input("Please enter your weight in kg: "))
    return weight

def getHeight():
    height = float(input("Please enter your height in m: "))
    return height

def BMI(ht, we):
    BMI=(we / (ht * ht))
    print ("Your BMI is :" , BMI)

    if BMI > 30 :
        print ("You are obese")
    elif BMI > 25 :
        print("You are overweight")
    elif BMI < 18.5 :
        print ("You are underweight")
    else:
        print ("You are healthy")
w = getWeight()
h = getHeight()
BMI(int(h), int(w))
