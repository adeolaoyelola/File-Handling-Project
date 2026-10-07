DIRECTORY = "c:\\TextFiles\\"
MESSAGE_TEXT_FILE = "messages.txt"
 
while True:
    print("\nSECRET AGENT MESSAGE SYSTEM")
    print("1. Append a message")
    print("2. Overwrite the file")
    print("3. Clear file content")
    print("4. Read all messages")
    print("5. delete the file")
    print("6. end program")
 
    choice = input("enter your choice: ")
 
    if choice == "1":
        message = input("Enter a message:")
 
        with open(f"{DIRECTORY}{MESSAGE_TEXT_FILE}", "at") as file:
            file.write(message + "\n")
 
        print("Message appended successfully!!")
 
    elif choice == "2":
        message = input("Enter a message:")
        
        with open(f"{DIRECTORY}{MESSAGE_TEXT_FILE}", "wt") as file:
            file.write(message + "\n")
 
        print(" File overwriten successfully")
 
    elif choice == "3":
        with open(f"{DIRECTORY}{MESSAGE_TEXT_FILE}", "wt") as file:
            file.write("")
 
        print("File content cleared successfully!")
 
    elif choice == "4":
        with open(f"{DIRECTORY}{MESSAGE_TEXT_FILE}", "rt") as file:
            messages = file.read()
 
            print("\nMessages:")
            print(messages)
 
            print("Messages read succesfully!")
 
    elif choice == "5":
        import os 
        os.remove(DIRECTORY + MESSAGE_TEXT_FILE)
 
        print("File deleted successfully!")
 
    elif choice == "6":
        print("Program ended.")
        break
 
    else:
        print("Invalid option. Please choose 1-6. ")