import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def __init__(self):
        # Twilio Setup
        self.twilio_sid = os.environ.get("TWILIO_SID")
        self.twilio_auth = os.environ.get("TWILIO_AUTH_TOKEN")
        self.twilio_phone = os.environ.get("TWILIO_PHONE")
        self.client = Client(self.twilio_sid, self.twilio_auth)

    def send_sms(self, message):
        """Send SMS alert"""
        try:
            message = self.client.messages.create(
                body=message,
                from_=self.twilio_phone,
                to=os.environ.get("YOUR_PHONE")
            )
            print(f"✅ SMS sent! SID: {message.sid}")
        except Exception as e:
            print(f"❌ SMS failed: {e}")

    def send_email(self, subject, body):
        """Send email alert (Optional)"""
        import smtplib
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(
                    os.environ.get("EMAIL"),
                    os.environ.get("APP_PASSWORD")
                )
                connection.sendmail(
                    from_addr=os.environ.get("EMAIL"),
                    to_addrs=os.environ.get("TO_EMAIL"),
                    msg=f"Subject: {subject}\n\n{body}"
                )
            print("✅ Email sent!")
        except Exception as e:
            print(f"❌ Email failed: {e}")