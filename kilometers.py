print("Leave the other field as 0.")
miles_o_km = input("Do you want to convert miles or kilometers? ")

miles = float(input("How many miles? "))
km = float(input("How many kilometers? "))


def m_to_km(miles):
    return miles * 1.60934

def km_to_m(km):
    return km / 1.60934

if miles_o_km == "miles":
    print("That is %f kilometers." % m_to_km(miles))
else:
    print("That is %f miles." % km_to_m(km))



