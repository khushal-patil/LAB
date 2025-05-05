import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

# Training data: (pattern, intent)
training_data = [
    ("hello", "greeting"),
    ("hi", "greeting"),
    ("hey", "greeting"),
    ("what products do you have", "products"),
    ("show me glasses", "products"),
    ("do you sell contact lenses", "products"),
    ("track my order", "track_order"),
    ("where is my order", "track_order"),
    ("order status", "track_order"),
    ("i want to return my glasses", "return_policy"),
    ("how to return", "return_policy"),
    ("what is your refund policy", "return_policy"),
    ("find store in Mumbai", "store_locator"),
    ("nearest store", "store_locator"),
    ("any shop in Delhi", "store_locator"),
    ("what offers are running", "offers"),
    ("any discounts", "offers"),
    ("show me promotions", "offers"),
    ("what lenses do you use", "faq"),
    ("are they anti glare", "faq"),
    ("do you offer scratch resistance", "faq"),
    ("help me", "help"),
    ("what can you do", "help"),
    ("bye", "goodbye"),
    ("thank you", "goodbye")
]

# Feature extractor
def extract_features(sentence):
    words = word_tokenize(sentence.lower())
    return {word: True for word in words}

# Prepare data
featuresets = [(extract_features(text), label) for (text, label) in training_data]

# Train the classifier
classifier = NaiveBayesClassifier.train(featuresets)

# Bot response templates
responses = {
    "greeting": ["Hello! Welcome to Lenskart.", "Hi there! How can I help you?"],
    "products": ["We offer eyeglasses, sunglasses, and lenses."],
    "track_order": ["Sure! Please provide your order ID (e.g., LK12345)."],
    "return_policy": ["We offer 14-day easy returns. The item must be unused."],
    "store_locator": ["Tell me your city, and I'll find the nearest store."],
    "offers": ["Buy 1 Get 1 Free on selected frames!"],
    "faq": ["Yes, our lenses have UV protection and anti-glare coating."],
    "help": ["You can ask about products, orders, returns, stores, or offers."],
    "goodbye": ["Thank you for visiting Lenskart!"],
    "fallback": ["I'm not sure I understand. Can you rephrase?"]
}

# Chat loop
print("Lenskart AI Assistant: Hello! Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Lenskart AI Assistant:", random.choice(responses["goodbye"]))
        break

    features = extract_features(user_input)
    predicted_intent = classifier.classify(features)

    response = random.choice(responses.get(predicted_intent, responses["fallback"]))
    print("Lenskart AI Assistant:", response)


