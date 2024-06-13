weight = input("What is your weight in lbs? ")
print(weight, "lbs")

h = input('Enter height in ft\'in": ')  # ask for input
h_split = h.split('\'')  # break string into 2 parts where single quote occurs
ft, inch = (h_split[0], h_split[1].split('"')[0])  # extract inches in a similar way
ft = int(ft)  # convert feet to integer
inch = int(inch)  # convert inches to integer
height = ft*12 + inch  # convert feet to inches and add inches


def calculate_bmi(weight, height):
    return (weight 
h = input('Enter height in ft\'in": ')  # ask for input
h_split = h.split('\'')  # break string into 2 parts where single quote occurs
ft, inch = (h_split[0], h_split[1].split('"')[0])  # extract inches in a similar way
ft = int(ft)  # convert feet to integer
inch = int(inch)  # convert inches to integer
height = ft*12 + inch  # convert feet to inches and add inches


def calculate_bmi(weight, height):
    return (weight / (height * height)) * 703

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
health_status = assess_health(bmi)/ (height * height)) * 703

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