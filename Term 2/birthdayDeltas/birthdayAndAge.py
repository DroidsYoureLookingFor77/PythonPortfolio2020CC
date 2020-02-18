import datetime

birthdayInput = input("Please type your birthday in the format YYYY-MM-DD: ") 

birthday = datetime.datetime.strptime(birthdayInput, "%Y-%m-%d")

now = datetime.datetime.now()

age = now - birthday

ageDays = age.days

ageYears = (age.days) / 365

birthWeekday = birthday

print("Your birthday is: " + str(birthday.date()))
print("You were born on a " + (birthWeekday.strftime("%A")))
print("You are ", ageDays, "days old.")
print(str.format("You are {0:.1f} years old.", ageYears))
