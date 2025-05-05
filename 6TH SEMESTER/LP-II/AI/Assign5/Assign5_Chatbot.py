import random
import re

# Chatbot identity
BOT_NAME = "Lenskart Assistant"

# Responses
responses = {
    "greeting": [
        "Hello! Welcome to Lenskart. How can I assist you today?",
        "Hi there! How can I help you with your eyewear needs?",
        "Welcome to Lenskart! What can I do for you?"
    ],
    "products": [
        "We offer eyeglasses, sunglasses, and contact lenses. Looking for anything specific?",
        "Our collection includes prescription glasses, blue light glasses, and stylish shades. Interested in any?",
        "We have computer glasses, zero power lenses, and more. Let me know what you need!"
    ],
    "track_order": [
        "Sure! Please provide your order ID (e.g., LK12345).",
        "I just need your order number to check the status. Please type it in."
    ],
    "track_order_followup": [
        "Thanks! Order ID {order_id} is on its way and should arrive in 2–3 days."
    ],
    "return_policy": [
        "We offer 14-day easy returns. The item must be unused and in original condition. Want to start a return?",
        "Most products are returnable within 14 days. Let me know if you’d like to begin the process."
    ],
    "store_locator": [
        "Sure! Please tell me your city and I’ll find the nearest store.",
        "Let me help. Which city are you in?"
    ],
    "store_locator_result": [
        "We have stores in {city}: Phoenix Mall, City Center, and Skyline Plaza. Visit anytime!"
    ],
    "offers": [
        "Right now, we’re offering *Buy 1 Get 1 Free* on select frames!",
        "Check out our latest deals on blue light glasses and power sunglasses!",
        "Students get an extra 10% off. Just show your ID in-store or apply the code STUDENT10 online!"
    ],
    "faq": [
        "Our lenses are made with high-index material and have UV protection.",
        "Yes, we provide anti-glare and scratch-resistant coatings on request.",
        "You can upload your prescription or visit the nearest store for a free eye test!"
    ],
    "help": [
        "You can ask me about products, track orders, locate stores, return policies, or available offers.",
        "Try asking things like 'Where is my order?', 'What are the offers?', or 'Return my glasses'."
    ],
    "goodbye": [
        "Thanks for visiting Lenskart! Stay stylish",
        "Glad to assist you. Have a wonderful day!",
        "Goodbye! Reach out anytime you need eyewear help."
    ],
    "fallback": [
        "Hmm, I didn't get that. Want to try asking differently?",
        "I'm a bit confused Can you clarify your question?",
        "Not sure how to help with that—maybe try 'help' to see what I can do."
    ]
}

# Keywords for intent detection
keywords = {
    "greeting": ["hello", "hi", "hey", "greetings"],
    "products": ["glasses", "sunglasses", "frames", "contact lenses", "buy", "product", "lenses"],
    "track_order": ["track", "status", "order", "delivery"],
    "return_policy": ["return", "exchange", "refund", "cancel"],
    "store_locator": ["store", "shop", "near", "location", "physical store", "city"],
    "offers": ["offer", "discount", "deal", "promo", "sale"],
    "faq": ["lens", "material", "scratch", "anti-glare", "prescription", "power", "coating", "uv"],
    "help": ["help", "support", "how", "can you", "what can"],
    "goodbye": ["bye", "goodbye", "thanks", "thank you", "exit"]
}

# Context memory
context = {
    "last_intent": None,
    "order_id": None,
    "city": None,
    "fallback_count": 0
}

def detect_intent(user_input):
    for intent, words in keywords.items():
        for word in words:
            if re.search(r'\b' + re.escape(word) + r'\b', user_input.lower()):
                return intent
    return "fallback"

def get_response(user_input):
    user_input = user_input.lower()

    # Handle store locator follow-up
    # Handle store locator follow-up
    if context["last_intent"] == "store_locator":
        known_cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Pune", "Chennai", "Kolkata", "Ahmedabad"]
        for city in known_cities:
            if city.lower() in user_input:
                context["last_intent"] = None
                return random.choice(responses["store_locator_result"]).format(city=city)
        
        # If no known city found, try to extract the last word (fallback method)
        words = user_input.strip().split()
        if words:
            possible_city = words[-1].capitalize()
            context["last_intent"] = None
            return random.choice(responses["store_locator_result"]).format(city=possible_city)


    # Handle order tracking follow-up
    if context["last_intent"] == "track_order":
        match = re.search(r'(lk\d{5,})', user_input)
        if match:
            order_id = match.group(1).upper()
            context["last_intent"] = None
            return random.choice(responses["track_order_followup"]).format(order_id=order_id)

    # Detect new intent
    intent = detect_intent(user_input)
    context["last_intent"] = intent

    if intent == "fallback":
        context["fallback_count"] += 1
        if context["fallback_count"] >= 2:
            context["fallback_count"] = 0
            return random.choice(responses["help"])
        return random.choice(responses["fallback"])

    context["fallback_count"] = 0
    return random.choice(responses[intent])

# Main loop
print(f"{BOT_NAME}: Hello! I'm your Lenskart helper. Type 'exit' to end the chat.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print(f"{BOT_NAME}: {random.choice(responses['goodbye'])}")
        break
    print(f"{BOT_NAME}: {get_response(user_input)}")
