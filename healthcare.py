import Convert

# Dictionary of patient information
patient = {"name": "Kevin", "lastname": "Cromley", "age": 22}


# Use import functions
weight = Convert.kg
height = Convert.m

print(weight, "kg")
print(height, "m")

# Function to calcualte BMI
def calculate_bmi(weight, height):
    return float(weight) / (float(height) ** 2)

# Function to assess health status
def assess_health(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

bmi = calculate_bmi(weight, height)
health_status = assess_health(bmi)


# Output
print("===================")
print("===================")
print("Patient Information")
print("===================")
print("===================")
print(patient["name"], patient["lastname"])
print(patient["age"], "Years old")
print("BMI:", bmi)
print("Health status:", health_status)
