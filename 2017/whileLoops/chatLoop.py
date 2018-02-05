message = input("Please enter a message.")

while message != "exit":
    print(message)
    message = input("Please enter a message.")
    if message == "abort":
        break
else:
    print("user has left the chat.")
    
