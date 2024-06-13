import json

json_string = [{"name": "Kevin", "lastname": "Cromley", "age": 22}]


ft = int(input("How many ft are you? "))
inch = int(input("How many inches are you? "))
inches = ft * 12 + inch
    

def weight():
    weight = input("What is your weight in lbs? ")
    print(weight, "lbs")


def bmi(weight, inches):
    return (weight / (inches ** 2)) * 703                                  


def health_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


print("===================")
print("===================")
print("Patient Information")
print("===================")
print("===================")


# Print patient information
print(json_string)
print("Your BMI and Health Satus:\n","BMI: ", bmi, "Health status:", health_status)