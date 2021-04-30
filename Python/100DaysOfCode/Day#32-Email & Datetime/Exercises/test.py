# SMTP EXERCISE
# import smtplib
#
#
# my_email = "tester19860221@gmail.com" password = "kiputX13" with smtplib.SMTP("smtp.gmail.com") as connection:
# connection.starttls() connection.login(user=my_email, password=password) connection.sendmail(from_addr=my_email,
# to_addrs="reizuki.nohara@gmail.com", msg="Subject: Test! \n\n Yo is this shit working?") connection.close()


# DATETIME EXERCISE
# import datetime as dt
#
# now = dt.datetime.now()
# date_of_birth = dt.datetime(year=1986, month=2, day=21)
# if now.year > 2020:
#     print("Yoos guys need an update!")
# print(now)


# MONDAY MOTIVATIONAL QUOTE!
# import smtplib
# import datetime as dt
# from random import choice
#
# my_email = 'tester19860221@gmail.com'
# password = 'kiputX13'
# now = dt.datetime.now()
# day_of_the_week = now.weekday()
# quotes = []
#
#
# if day_of_the_week == 0:
#
#     with open('../quotes.txt', 'r') as file:
#         data = file.readlines()
#         for line in data:
#             quotes.append(line)
#             quote = choice(quotes)
#
#     with smtplib.SMTP('smtp.gmail.com') as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#         from_addr=my_email,
#         to_addrs='reizuki.nohara@gmail.com',
#         msg=f"Subject: Motivation \n\n{quote}")
