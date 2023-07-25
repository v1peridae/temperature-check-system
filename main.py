# Task 1
print("TASK 1", "\n")
temp = float(input("Enter the temperature in degrees Celsius >>> "))
if temp >= 22 or temp <= 24:
    print("Temperature is within the acceptable range.", "\n")
elif temp > 24:
    print("Temperature is too high. Cooling activated.", "\n")
else:
    print("Temperature is too low. Heating activated.","\n")

# Task 2
print("TASK 2""\n")
five_hour_temp = []

temp = float(input("The temperature at the 1st hour >>>"))
five_hour_temp.append(temp)
temp = float(input("The temperature at the 2nd hour >>>"))
five_hour_temp.append(temp)
temp = float(input("The temperature at the 3rd hour >>>"))
five_hour_temp.append(temp)
temp = float(input("The temperature at the 4th hour >>>"))
five_hour_temp.append(temp)
temp = float(input("The temperature at the 5th hour >>>"))
five_hour_temp.append(temp)
"\n"

max_temp = max(five_hour_temp)
min_temp = min(five_hour_temp)
temp_difference = max_temp - min_temp

print("Highest temperature: ",max_temp,"°C")
print("Lowest temperature: ",min_temp,"°C")
print("Temperature range:", temp_difference,"°C","\n")

# Task 3
print("TASK 3""\n")
count_high = 0
count_low = 0

for x in range(5):
  if five_hour_temp[x] > 24:
        print("Hour",x+1, "- Temperature was too high.")
  elif five_hour_temp[x] < 22:
        print("Hour",x+1, "- Temperature was too low.")
  else:
        print("Hour",x+1,"- Temperature was within the acceptable range.")
