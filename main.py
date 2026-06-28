import random
import datetime
import pandas
import smtplib

dob = pandas.read_csv("dob_file.csv")

today = datetime.datetime.now()

for index,row in dob.iterrows():
    if today.month == row["month"] and today.day == row["day"]:
        with open("letter1") as file:
            letter1 = file.read()
        with open("letter2") as file:
            letter2 = file.read()
        with open("letter3") as file:
            letter3 = file.read()
        letters = [letter1, letter2, letter3]
        random_letter = random.choice(letters)
        name = row["name"]

        my_email = ""
        password = ""

        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(to_addrs=row["email"],from_addr=my_email,msg=f"Subject:Hello{name}\n\n{random_letter}")






