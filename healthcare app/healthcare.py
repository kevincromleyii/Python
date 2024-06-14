import Convert
import json

# Dictionary of patient information
json_string = [{"name": "Kevin", "lastname": "Cromley", "age": 22}]

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

json_strings_2 = ["BMI: ", bmi, "Health status: ", health_status]


# Output
print("===================")
print("===================")
print("Patient Information")
print("===================")
print("===================")
print(json_string)
print(json_strings_2)

# Save the patient information to a file
with open('patient_infos.json', 'w') as f:
    json.dump(json_string, f)
    json.dump(json_strings_2, f)
    print("Patient information saved to file.")
 