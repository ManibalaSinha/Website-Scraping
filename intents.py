intents = {
    "greet": {
        "examples": ["hello", "hi", "hey"],
        "response": "Hello! How can I help you today?"
    },
    "goodbye": {
        "examples": ["bye", "goodbye", "see you"],
        "response": "Goodbye! Have a nice day!"
    },
    "thanks": {
        "examples": ["thank you", "thanks"],
        "response": "You're welcome!"
    }
}
def get_intent(user_input):
    for intent, data in intents.items(): #Loop through each intent in intents dictionary,intent is key like greet,data contains example 
        for example in data["examples"]: # for each example phrase under that intent, loop through them
            if example in user_input.lower(): #check if example is contained inside user's input
                return intent
    return "unknown" # if no intent matches any example phrase, return "unknown"

def get_response(user_input):
    intent = get_intent(user_input) # call the get_intent() function to find out which intent matches user input
    if intent in intents: #check if exists in intents dictionary
        return intents[intent]["response"] #return predefined response for the matched intent
    else:
        return "Sorry, I didn't understand that."

# Example:
user_message = input("You: ") # get user input from the terminal
bot_response = get_response(user_message) #pass the user input to the bot to get a response
print("Bot:", bot_response)
