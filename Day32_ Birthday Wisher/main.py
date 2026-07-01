##################### Normal Starting Project ######################
from datetime import datetime
import pandas
import random
import smtplib
today = datetime.now()
today_tuple = (today.month, today.day)

myemail= "xayehe3822@icotz.com"
pass = "12345678"

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open (file_path) as letter_file:
        contents = letter_file.read()
        content=  contents.replace("[Name]",birthday_person["name"])
    with smtplib.SMPT("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(myemail, pass)
        connection.sendmail(
            from_addr = myemail, 
            to_addrs = birthday_person["email"],
            msg = f"Subject : Happy Birthday! \n\n{content}")




