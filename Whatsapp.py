import pywhatkit
import datetime

# Get Current Hour and Minute
now = datetime.datetime.now()
hour = now.hour
minute = now.minute
minute+=1

# Get Message Text
file = open("Message.txt")
line = file.read()
file.close()
print(line)
message = str(line)

# For more formatting try out the below options like adding Emoticons, newlines, images (for that please use different method in pywhatkit) etc.
# message = '''Hello user  \U0001F600 \n 
# Good morning!
# This is an automatic message from script \U0001F600 '''
# message = str(message)


# Iterate through the Phone numbers given in PhoneNumbers.txt and send the message by opening Whatsapp in browser.
# Pre-requisite: Whatsapp Web should be logged-in already in web browser
with open("PhoneNumbers.txt") as file:
    for item in file:
        minute +=1
        pywhatkit.sendwhatmsg(str(item.strip()), message, hour,minute)