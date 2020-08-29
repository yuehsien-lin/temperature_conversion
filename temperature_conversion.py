# Input a temperature value in Celsius
# then print a temperature value in Fahrenheit

tempC = input('Please input the temperature (in Celsius degree): ')
tempC = int(tempC)
tempF = tempC * 9 / 5 + 32
tempF = float(tempF)
print('The temperature is ', tempF, ' (in Fahrenheit degree)')