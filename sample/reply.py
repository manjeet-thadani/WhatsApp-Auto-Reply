import time
import MySQLdb
from time import gmtime, strftime
from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="Quotes")        # name of the data base

cur = db.cursor()
driver = WhatsAPIDriver()
print("Waiting for QR")
driver.wait_for_login()

print("Bot started")

while True:
    time.sleep(3)
    print('Checking for more messages')
    for contact in driver.get_unread():
        for message in contact.messages:
            if isinstance(message, Message): # Currently works for text messages only.
                message_received= message.safe_content
                message_to_send = ""
                cur.execute("SELECT * FROM Quotes ORDER BY RAND() LIMIT 1;")
                for row in cur.fetchall():
                    message_to_send = row[0]
                if "-" not in contact.chat.id.split("@")[0]:
                    contact.chat.send_message(message_to_send)
                    contact_number = contact.chat.id.split("@")[0]
                    curr_date_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                    status = "Success"

                    sql = "insert into Logs(number, dateTime, incomingMessage, messageSent, status) VALUES(%d, '%s', '%s', '%s', '%s')" % \
     (int(contact_number), curr_date_time , message_received, message_to_send, status)
                    cur.execute(sql)
                    db.commit()
