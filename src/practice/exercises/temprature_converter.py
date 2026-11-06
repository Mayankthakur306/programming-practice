## Task: Prompt the user for a temperature in Celsius and 
# convert it to Fahrenheit using the formula:
# F = (C*9/5) + 32
# Key concepts: input(), float(), arithmetic operations, print().

temperature = float(input("Enter the temp in c: "))
fahrenheit = (temperature*9/5) + 32

print("the temprature in farenheit: ",fahrenheit)