"""
Andie Goode
11/28/15
Function:KFC Temperatures
"""
#create function displayWelcome
def displayWelcome():
    print('This program will convert temperatures')
    print('Enter (F) to convert Fahrenheit to Celsius')
    print('Enter (C) to convert Celsius to Fahrenheit')
    print('Enter (C2) to convert Kelvin to Celsius')
    print('Enter (K) to convert Celsius to Kelvin')
    print('')
#create function getConvertTo
def getConvertTo():
    #prompt user for selection until valid selection and return which
    which = input('Enter selection: ')
    while which != 'F' and which != 'K' and which != 'C' and which != 'C2':
        which = input('Enter selection: ')
    return which
#create function FahrenToCelsius
def FahrenToCelsius(x):
    convert_temp = (x - 32) * (5/9)
    return round(convert_temp,2)
#create function CelsiusToFahren
def CelsiusToFahren(x):
    convert_temp = ((9/5) * x) + 32
    return round(convert_temp,2)
#create function KelvinToCelsius
def KelvinToCelsius(x):
    convert_temp = x - 273.15
    return round(convert_temp,2)
#create function CelsiusToKelvin
def CelsiusToKelvin(x):
    convert_temp = x + 273.15
    return round(convert_temp,2)
#create function main
def main():
    # Display program welcome
    displayWelcome()
    # Get which conversion from user
    which = getConvertTo()
    # Get the temperature to convert
    temp = int(input('Enter the temperature to convert: '))
    # Display the converted temperature
    if which == 'F':
        print(FahrenToCelsius(temp))
    elif which == 'C':
        print(CelsiusToFahren(temp))
    elif which == 'C2':
        print(KelvinToCelsius(temp))
    elif which == 'K':
        print(CelsiusToKelvin(temp))
#call main function
main()
