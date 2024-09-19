"""
String Formatting
"""


first_name = "Eric"

sentence = "Hi {} {}"
last_name = "Roby"
print(sentence.format(first_name, last_name))

print(f"Hi {first_name} {last_name} I hope you are learning")


'''
String Assignment we will do together:

Ask the user how many days until their birthday
and print an approx number of weeks until their birthday

Weeks is = 7 days

decimals within the return is allowed..
'''


days = int(input("How many days until your birthday? "))

print(round(days/7, 2))