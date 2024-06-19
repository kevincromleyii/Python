import Convert
import json
import pandas as pd

name = input("Enter Patients name: ")
lastname = input("Enter Patients lastname: ")
age = input("Enter Patients age: ")

# Dictionary of patient information
patient_info = {
    "name:": name, 
    "lastname:": lastname,
    "age:": age,
}

json_info = json.dumps(patient_info, indent=4)

# Use import functions
weight = Convert.kg
height = Convert.m

print(f"Weight: {weight} kg")
print(f"Height: {height} m")

# Function to calcualte BMI
def calculate_bmi(weight, height):
    return float(weight) / (float(height) ** 2)

# Function to assess health status
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Function to assess health status based on BMI
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

patient_info["BMI"] = bmi
patient_info["Health status:"] = health_status

json_2 = json.dumps(patient_info, indent=4)

# Create a DataFrame with patient information
df_data = {
    "Name": [name],
    "Lastname": [lastname],
    "Age": [age],
    "Weight": [weight],
    "Height": [height],
    "BMI": [bmi],
    "Health Status": [health_status]
}

df = pd.DataFrame(df_data)

print("===================")
print("Patient Information DataFrame")
print("===================")
print(df)

# Writing patient information DataFrame to a JSON file
df.to_csv("patient_info.csv", index=False)
