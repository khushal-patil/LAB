import datetime
print("Welcome to the Ab's Restaurant\n")
print("I'm your personal assistant. You can ask me about menu , prices , timings , contact details or reservations.")
print("If you want futhter detailed information -- type help")

def help():
    print("""\nHere's somethings you can ask me about
    - "menu"->Show menu options
    -"prices"/"cost"->show me the average cost
    -"contact/"phone"->Provide me contact details
    -"timings"-> What are the timings
    -"reservation"-> Reservation info
    -"exit"->exit""")

while True:
    user_input= input("\nYou:").lower()

    if "menu" in user_input :
        print("Chatbot: We have variety of cuisines as Indian , Mexican , Italian , Chinese etc...")
    elif "price" in user_input or "how much" in user_input or "cost" in user_input:
        print("Chatbot: The average cost for 2 people is 500 rs .")
    elif "contact" in user_input or "phone" in user_input:
        print("Chatbot:You can contact with us on 91-8262162861.")
    elif "hours" in user_input:
        print("Chatbot:We are at service from 9 AM to 12 PM . Monday - Sunday.")
    elif "reservations" in user_input or "bookings" in user_input:
        print("Chatbot: You can reserve your table by contating us on 91-8262162861 or by visiting our website Ab'srest.org ")
    elif "date" in user_input or "time" in user_input:
        now = datetime.datetime.now()
        print(f"Chatbot: Today's date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}.")
    elif "help" in user_input:
        help()
    elif "sup"in user_input or "hello" in user_input or "meow" in user_input:
        print("Chatbot:Hello There !! How can i Help u?")
    elif "exit" in user_input:
        print("Chatbot:Thank you for your inquiry . Enjoy your day")
        break
    else:
        print("Chatbot:Please enter valid input.")
