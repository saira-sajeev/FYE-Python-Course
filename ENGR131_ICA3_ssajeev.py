def check_message(message):
    if not message:
        return "You didn't enter anything!"
    else:
        return f"You entered: {message}"

message = input("Enter something: ")
print(check_message(message))
