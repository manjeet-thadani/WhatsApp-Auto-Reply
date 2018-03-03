import requests
import time
from time import gmtime, strftime
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message

driver = WhatsAPIDriver()
print("Waiting for QR")
driver.wait_for_login()

print("Bot started")

while True:
    time.sleep(3)
    print('Checking for more messages')
    for contact in driver.get_unread():
        print("msg received")
        for message in contact.messages:
            
            try:
                if "-" not in contact.chat.id.split("@")[0]: #only for personal messages
                    message_received= message.safe_content
                    contact_number = contact.chat.id.split("@")[0]
                    message_to_send = 'hello there'
                    contact.chat.send_message(message_to_send)
                    
            except:
                print("Error Occured")
