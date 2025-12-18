name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = round(weight / (height ** 2))
print(f"Your BMI is: {bmi}")

if bmi > 0 :
    if bmi < 18.5 :
        print(name + ", you are underweight.")
    elif bmi <= 24.9 :
        print(name + ", you have a normal weight.")
    elif bmi <= 29.9 :
        print(name + ", you are overweight.")
    elif bmi <= 34.9 :
        print(name + ", you are obese.")
    elif bmi <= 39.9 :
        print(name + ", you are severely obese.")
    else :
        print(name + ", you are morbidly obese.")
else :
    print("Invalid BMI calculated.")
