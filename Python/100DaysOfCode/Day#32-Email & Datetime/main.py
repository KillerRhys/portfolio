import random

import pandas
import smtplib
from datetime import datetime as dt
from random import choice

my_email = 'email'
password = "pass"
check = (dt.now().month, dt.now().day)
data = pandas.read_csv('birthdays.csv')
new_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if check in new_dict:
    party_animal = new_dict[check]
    file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'
    with open(file_path) as letter:
        stuff = letter.read()
        stuff.replace("[NAME]", party_animal["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=party_animal['email'],
            msg=f"Subject:Happy Birthday \n\n {stuff}"
        )


