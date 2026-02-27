print("I'll help you to covert temparature")

print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")
print("3: Celsius to Kelvin")
print("4: Kelvin to Celsius")
print("5: Fahrenheit to Kelvin")
print("6: Kelvin to Fahrenheit")
choice=input("Choose a conversion from above options:")
print("you have selected the option:", choice)

temp=float(input("please enter the value to conversion: "))



def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32
if choice=="1":
    result=celsius_to_fahrenheit(temp)
    print("converted value", result)
elif choice=="2":
    result =fahrenheit_to_celsius(temp)
    print("converted value", result)
elif choice=="3":
    result =celsius_to_kelvin(temp)
    print("converted value", result)
elif choice=="4":
    result =kelvin_to_celsius(temp)
    print("converted value", result)
elif choice=="5":
    result =fahrenheit_to_kelvin(temp)
    print("converted value", result)
elif choice=="4":
    result =kelvin_to_fahrenheit(temp)
    print("converted value", result)