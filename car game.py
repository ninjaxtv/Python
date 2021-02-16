command = ""
while command.lower() != "quit":
    command = input("> ").lower()
    if command == "start":
        print("Car has started!!")
    elif command == "stop":
        print("car stopped.")
    elif command == "help":
        print("""
        start = to start the car
        stop = to stop the car
        quit = to quit
        """)
    elif command == "quit":
         print("done!!")
    else:
        print("Sorry invalid")




















    
