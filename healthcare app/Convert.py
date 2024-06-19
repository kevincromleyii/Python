def lbs_to_kg(lbs):
    return float(lbs) * 0.453592

# Test the function
lbs = input("Enter weight in lbs: ")
kg = lbs_to_kg(lbs)
print(f"{lbs} lbs is equal to {kg} kg.")



def ft_to_m(ft):
    return float(ft) * 0.3048
    

ft = input("Enter height in ft: ")
m = ft_to_m(ft)
print(f"{ft} ft is equal to {m} m.")