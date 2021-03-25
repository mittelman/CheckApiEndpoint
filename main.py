import requests
import telegram_send

# api-endpoint
URL = "http://google.com"

# default message
message = "Your app is working! :)"

try:
    # send a request and get a response
    r = requests.get(url=URL)
except requests.ConnectionError as exception:
    # URL is not valid
    message = "Your app is not working! :("
finally:
    # send a telegram message and print the message
    telegram_send.send(messages=[message])
    print(message)