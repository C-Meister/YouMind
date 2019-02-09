import nativemessaging

while True:
    message = nativemessaging.get_message()
    print(message)
