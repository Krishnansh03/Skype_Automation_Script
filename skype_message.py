import schedule
import time
from datetime import datetime
from skpy import Skype
import os

# Get Skype credentials from environment variables
skype_username = os.getenv('SKYPE_USERNAME')
skype_password = os.getenv('SKYPE_PASSWORD')
chat_id = os.getenv('SKYPE_CHAT_ID')

# Create a Skype instance and login
sk = Skype(skype_username, skype_password)

def send_checkin_message():
    if datetime.today().weekday() < 5:  # 0 = Monday, 1 = Tuesday, ..., 4 = Friday
        chat = sk.contacts[chat_id].chat
        chat.sendMsg("Check-in: Good morning! I'm starting my work day.")

def send_checkout_message():
    if datetime.today().weekday() < 5:  # 0 = Monday, 1 = Tuesday, ..., 4 = Friday
        chat = sk.contacts[chat_id].chat
        chat.sendMsg("Check-out: Good evening! I'm finishing my work day.")


# Schedule the messages for weekdays
schedule.every().monday.at("10:00").do(send_checkin_message)
schedule.every().tuesday.at("10:00").do(send_checkin_message)
schedule.every().wednesday.at("10:00").do(send_checkin_message)
schedule.every().thursday.at("10:00").do(send_checkin_message)
schedule.every().friday.at("10:00").do(send_checkin_message)

schedule.every().monday.at("18:00").do(send_checkout_message)
schedule.every().tuesday.at("18:00").do(send_checkout_message)
schedule.every().wednesday.at("18:00").do(send_checkout_message)
schedule.every().thursday.at("18:00").do(send_checkout_message)
schedule.every().friday.at("18:00").do(send_checkout_message)

# def send_one_time_message():
#     one_time_chat_id = 'recipient_skype_username'  # Replace with the recipient's Skype username                                          
#     chat = sk.contacts[one_time_chat_id].chat
#     chat.sendMsg("This is a one-time message sent at 12:10 PM today.")
#     print("One-time message sent")

# Schedule the one-time message for today at 12:10 PM
schedule.every().day.at("12:10").do(send_one_time_message)

while True:
    schedule.run_pending()
    time.sleep(1)
