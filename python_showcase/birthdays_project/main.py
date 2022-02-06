
import pandas
import random
import smtplib
import datetime as dt

data = pandas.read_csv("birthdays.csv")
bday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

now = dt.datetime.now()
today_tuple = (now.month, now.day)

birthday_person = bday_dict[today_tuple]
bday_email = birthday_person["email"]


my_email = "kylepythontestemail@gmail.com"
password = "pythontest"

if today_tuple in bday_dict:
    birthday_person = bday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_contents = contents.replace("[NAME]", birthday_person["name"])
    print(new_contents)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=bday_email,
                            msg=f"Subject: Happy Birthday!\n\n{new_contents}")
