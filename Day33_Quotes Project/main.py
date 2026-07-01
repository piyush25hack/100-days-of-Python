import smtplib
import datetime as dt
import random 

my_email = "yapike6594@gmail.com"
password = "rbos xyhj jwjl tigv" # Make sure this is an App Password

now = dt.datetime.now()
weekday = now.weekday()
print(f"Today is weekday number: {weekday}") # Ye debug ke liye hai

if weekday == 0:  # 0 is Monday
    print("It's Monday! Sending email...") # Ye confirm karega ki if ke andar gaye
    with open("./quotes.txt") as quote_file:
        quotes_01 = quote_file.readlines()
        quote = random.choice(quotes_01)
        
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls() 
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
    print("Email sent successfully!")
else:
    print("Today is not Monday, so no email was sent.")