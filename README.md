# Skype Attendance Automation

This project automates daily Skype check-in and check-out messages for attendance purposes. It sends a check-in message at 10:00 AM and a check-out message at 6:00 PM on weekdays (Monday to Friday). Additionally, it can send a one-time message at a specified time.

## Features

- Automated check-in and check-out messages on weekdays.
- One-time message sending functionality.
- Easy configuration via environment variables.

## Requirements

- Python 3
- Termux (for Android users)
- Skype account

## Setup Instructions

1. **Clone the Repository:**

   ```sh
      git clone https://github.com/krishnnsh03/SkypeAttendance.git
   ```

2. **Install Dependencies:**

   Ensure you have Python installed. Then, install the required Python packages using pip:

   ```sh
       pip install -r requirements.txt
   ```

3. Set Environment Variables:

   Set your Skype credentials and the chat ID of the recipient in your environment variables. In Termux, you can do this by running:
   
   ```sh
   
      export SKYPE_USERNAME="your_skype_username"  ## or email
      export SKYPE_PASSWORD="your_skype_password"  
      export SKYPE_CHAT_ID="your_chat_id_or_recipient_username"
   ```

   for getting recipient's Chatid add the following in your script...

   ```py
      sk = Skype(skype_username, skype_password)
      contacts = sk.contacts
      for i in contacts:
          print(i)
          print("\n")
   ```
   
5. Edit the Script (Optional):

   If you want to change the recipient of the one-time message, edit the send_one_time_message function in skype_attendance.py and replace          'recipient_skype_username' with the actual Skype username of the recipient.

6. Run the Script:

   Run the script to start the automation:

   ```sh
      python skype_attendance.py
   ```
