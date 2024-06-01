import pandas
import smtplib
import datetime as dt
import random


with open("letter_1.txt") as letter1:
    letter_file = letter1.read()

with open("letter_2.txt") as letter2:
    letter_file2 = letter2.read()

with open("letter_3.txt") as letter3:
    letter_file3 = letter3.read()
letters = [letter_file,letter_file2,letter_file3]
random_letter = random.choice(letters)

birthdays = pandas.read_csv("birthdays.csv")
names = birthdays.name.to_list()
mails = birthdays.email.to_list()
print(birthdays)
email = "bookmybus.info@gmail.com"
password = "keqe hieq rgzp brwa"

def mail():
    date = dt.datetime.today().replace(microsecond=0)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="rtpurpose123@gmail.com",
                            msg=f"Subject:Booking Confirmed - BookMyBus\n\n"
                                f"Your Booking has been confirmed by BookMyBus on {date}."
                                f" Hope you enjoyed the experience."
                            )


def letter():
    PLACEHOLDER = "[NAME]"
    random_letter
    for name in names:
        stripped_name = name.strip().title()
        new_letter = letter_file.replace(PLACEHOLDER, stripped_name)
        with open(f"{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)


