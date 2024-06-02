import pandas
import smtplib
import datetime as dt
import random


with open("letter_1.txt") as letter1:
    letter_file1 = letter1.read()

with open("letter_2.txt") as letter2:
    letter_file2 = letter2.read()

with open("letter_3.txt") as letter3:
    letter_file3 = letter3.read()

letters = [letter_file2,letter_file3]


birthdays = pandas.read_csv("birthdays.csv")
email = "example@email.com" # // put your email
password = "############" # // put your app generated password from google account

current_date = dt.date.today()
current_month = current_date.month
current_day = current_date.day

check_birthdays = birthdays[(birthdays['month'] == current_month) & (birthdays['day'] == current_day)]
names = check_birthdays.name.to_list()
mails = check_birthdays.email.to_list()


class Birthday_wishher:

    def letter(self):
        PLACEHOLDER = "[NAME]"
        for name in names:
            random_letter = random.choice(letters)
            stripped_name = name.strip().title()
            new_letter = random_letter.replace(PLACEHOLDER, stripped_name)
            with open(f"{stripped_name}.txt", mode="w") as completed_letter:
                completed_letter.write(new_letter)

    def emails(self):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            for name in names:
                self.letter()
                check_email = birthdays[birthdays['name'] == name]
                filtered_email = check_email.email.to_list()
                name_titled = name.title()
                with open(f"{name_titled}.txt") as file:
                    letter = file.read()
                    connection.sendmail(from_addr=email,
                                        to_addrs=filtered_email,
                                        msg=f"Subject:Happy Birthday {name_titled} - BookMyBus\n\n"
                                            f"{letter}"
                                        )

bw = Birthday_wishher()
bw.emails()
